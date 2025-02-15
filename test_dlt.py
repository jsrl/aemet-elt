import dlt
import http.client
import json
import os
import requests
from dotenv import load_dotenv

# Cargar el archivo .env
load_dotenv()
# Obtener la API key de la variable de entorno
api_key = os.getenv("API_KEY")

# Establece las credenciales de GCP
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys/creds.json"
os.environ["API_AEMET_TO_GCS__DESTINATION__BUCKET_URL"] = "gs://taxis-bucket-448121-i4/test-dlt"

# Configura la pipeline para escribir en GCS
pipeline = dlt.pipeline(
    pipeline_name="api_aemet_to_gcs",
    destination="filesystem",  # Usamos "filesystem" como destino
    dataset_name="test_dlt"
)

# Función para extraer datos de la API
def extract_data():
    conn = http.client.HTTPSConnection("opendata.aemet.es")
    headers = {
        'cache-control': "no-cache"
    }
    conn.request("GET", f"/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/?api_key={api_key}", headers=headers)
    res = conn.getresponse()
    data = res.read()
    response_json = json.loads(data.decode("utf-8"))
    
    # Obtener la URL del campo 'datos'
    datos_url = response_json.get("datos")
    
    # Hacer una segunda solicitud a la URL obtenida
    response = requests.get(datos_url)
    response.raise_for_status()
    data = response.json()
    
    for record in data:
        yield record

# Usar dlt para cargar datos desde la URL obtenida
resource = dlt.resource(extract_data, name="api_data")

# Ejecuta la carga en GCS
load_info = pipeline.run(resource, loader_file_format="parquet")
print(load_info)

