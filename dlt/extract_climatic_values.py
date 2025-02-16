import dlt
import http.client
import json
import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta

# Load the .env file for the AEMET_API_KEY
load_dotenv()
api_key = os.getenv("AEMET_API_KEY")

# Set GCP credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys/creds.json"
os.environ["CLIMATIC_VALUES_TO_GCS__DESTINATION__BUCKET_URL"] = "gs://taxis-bucket-448121-i4"

# Configure the pipeline to write to GCS
pipeline = dlt.pipeline(
    pipeline_name="climatic_values_to_gcs",
    destination="filesystem",
    dataset_name="climatic_values"
)

# Parameter: year to extract data
year = 2024

# Generate start and end dates for the specified year
start_date = datetime(year, 1, 1)
end_date = datetime(year, 12, 31)

# Function to extract data from the API in 15-day intervals
def extract_data():
    current_date = start_date
    while current_date <= end_date:
        # Calculate the end date for this 15-day interval
        interval_end_date = current_date + timedelta(days=14)
        # Ensure the end date does not exceed the specified end date
        if interval_end_date > end_date:
            interval_end_date = end_date
        
        # Format the dates as strings in the required format
        start_date_str = current_date.strftime("%Y-%m-%dT%H:%M:%SUTC")
        end_date_str = interval_end_date.strftime("%Y-%m-%dT%H:%M:%SUTC")

        print(f"Extracting data for the interval: {start_date_str} - {end_date_str}")

        # Make the API request
        conn = http.client.HTTPSConnection("opendata.aemet.es")
        headers = {
            'cache-control': "no-cache"
        }
        conn.request("GET", f"/opendata/api/valores/climatologicos/diarios/datos/fechaini/{start_date_str}/fechafin/{end_date_str}/todasestaciones?api_key={api_key}", headers=headers)
        res = conn.getresponse()
        data = res.read()
        response_json = json.loads(data.decode("utf-8"))
        
        # Get the URL from the 'datos' field
        datos_url = response_json.get("datos")        
        if datos_url:
            # Make a second request to the obtained URL
            response = requests.get(datos_url)
            response.raise_for_status()
            data = response.json()
            
            for record in data:
                yield record

        # Update the start date for the next interval
        current_date = interval_end_date + timedelta(days=1)

resource = dlt.resource(extract_data, name="climatic_values")
# Run the pipeline to load data into GCS
load_info = pipeline.run(resource, loader_file_format="parquet", write_disposition="replace")

row_counts = pipeline.last_trace.last_normalize_info
print(row_counts)
print("------")
print(load_info)
