import http.client
import json
import requests
#import dlt

api_key = "eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJqb3NlLmx1aXMucm9zZWxsby5mZXJyZXJAZ21haWwuY29tIiwianRpIjoiOWRhOTU1NTgtNWE4NS00ZWRiLTgzNmYtZmU0NDQ2MjRlMTFhIiwiaXNzIjoiQUVNRVQiLCJpYXQiOjE3Mzk2MzAwNjUsInVzZXJJZCI6IjlkYTk1NTU4LTVhODUtNGVkYi04MzZmLWZlNDQ0NjI0ZTExYSIsInJvbGUiOiIifQ.64xa7Ah84HmWEIo9lyT4ycE7l2oVvSpE0bPTpJLk7a8"
conn = http.client.HTTPSConnection("opendata.aemet.es")

headers = {
    'cache-control': "no-cache"
    }

conn.request("GET", f"/opendata/api/valores/climatologicos/inventarioestaciones/todasestaciones/?api_key={api_key}", headers=headers)

res = conn.getresponse()
data = res.read()

# Decodificar y analizar la respuesta JSON
response_json = json.loads(data.decode("utf-8"))

# Obtener la URL del campo 'datos'
BASE_API_URL = response_json.get("datos")

print(BASE_API_URL)

# Usar dlt para cargar datos desde la URL obtenida
response = requests.get(BASE_API_URL)
response.raise_for_status()
data = response.json()

# Procesar los datos obtenidos
print(data)