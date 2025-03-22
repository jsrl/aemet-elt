import dlt
import http.client
import json
import os
import requests
from dotenv import load_dotenv

# Load the .env file for the AEMET_API_KEY
load_dotenv()
api_key = os.getenv("AEMET_API_KEY")

# Set GCP credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys/creds.json"
os.environ["WEATHER_STATIONS_TO_GCS__DESTINATION__BUCKET_URL"] = "gs://aemet-weather-data-bucket"

# Configure the pipeline to write to GCS
pipeline = dlt.pipeline(    
    import_schema_path="dlt/schemas/import",
    export_schema_path="dlt/schemas/export",
    pipeline_name="weather_stations_to_gcs",
    destination="filesystem",  # Use "filesystem" as the destination
    dataset_name="weather_stations"
)

# Function to extract data from the API
def extract_data():
    conn = http.client.HTTPSConnection("opendata.aemet.es")
    headers = {
        'cache-control': "no-cache"
    }
    conn.request("GET", f"/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones?api_key={api_key}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    response_json = json.loads(data.decode("utf-8"))
    
    # Get the URL from the 'datos' field
    datos_url = response_json.get("datos")
    
    # Make a second request to the obtained URL
    response = requests.get(datos_url)
    response.raise_for_status()
    data = response.json()
    
    for record in data:
        yield record

# Use dlt to load data from the obtained URL
resource = dlt.resource(extract_data, name="weather_stations")

# Run the pipeline to load data into GCS
load_info = pipeline.run(resource, loader_file_format="parquet", write_disposition="replace")

# Print the schema of the pipeline
# print(pipeline.default_schema.to_pretty_yaml())

row_counts = pipeline.last_trace.last_normalize_info
print(row_counts)
print("------")
print(load_info)