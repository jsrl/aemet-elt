import dlt
import http.client
import json
import os
import requests
from dotenv import load_dotenv
from datetime import datetime, timedelta

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

# Parámetro: año para extraer los datos
year = 2024

# Generar fechas de inicio y fin para el año especificado
fecha_inicio = datetime(year, 1, 1)
fecha_fin = datetime(year, 12, 31)

# Función para extraer datos de la API en intervalos de 15 días
def extract_data():
    current_date = fecha_inicio
    while current_date <= fecha_fin:
        # Calculamos la fecha de fin para este intervalo de 15 días
        end_date = current_date + timedelta(days=14)
        
        # Formatear las fechas a string en el formato necesario
        fechaIniStr = current_date.strftime("%Y-%m-%dT%H:%M:%SUTC")
        fechaFinStr = end_date.strftime("%Y-%m-%dT%H:%M:%SUTC")

        print(f"Extrayendo datos para el intervalo: {fechaIniStr} - {fechaFinStr}")

        # Realizar la solicitud a la API
        conn = http.client.HTTPSConnection("opendata.aemet.es")
        headers = {
            'cache-control': "no-cache"
        }
        conn.request("GET", f"/opendata/api/valores/climatologicos/diarios/datos/fechaini/{fechaIniStr}/fechafin/{fechaFinStr}/todasestaciones?api_key={api_key}", headers=headers)
        res = conn.getresponse()
        data = res.read()
        response_json = json.loads(data.decode("utf-8"))
        
        # Obtener la URL del campo 'datos'
        datos_url = response_json.get("datos")
        
        if datos_url:
            # Hacer una segunda solicitud a la URL obtenida
            response = requests.get(datos_url)
            response.raise_for_status()
            data = response.json()
            
            for record in data:
                yield record

        # Actualizar la fecha de inicio para el siguiente intervalo
        current_date = end_date + timedelta(days=1)

# Usar dlt para cargar datos desde la URL obtenida
resource = dlt.resource(extract_data, name="api_data")

# Ejecuta la carga en GCS
load_info = pipeline.run(resource, loader_file_format="parquet", write_disposition="replace")

row_counts = pipeline.last_trace.last_normalize_info
print(row_counts)
print("------")
print(load_info)
