from dlt.sources.filesystem import readers
import dlt
import os
from dlt.destinations.adapters import bigquery_adapter

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys/creds.json"

def load_data_to_bq(bucket_url, pipeline_name, table_name, partition_field=None):
    print(f"Starting load for {table_name}...")
    pipeline = dlt.pipeline(
        pipeline_name=pipeline_name,
        destination="bigquery", 
        dataset_name="weather_dataset",
    )
    
    parquet_reader = readers(bucket_url, file_glob="**/*.parquet").read_parquet()
    load_info = pipeline.run(bigquery_adapter(parquet_reader.with_name(table_name), autodetect_schema=True, partition=partition_field), 
                             write_disposition="replace")
    print(load_info)
    print(pipeline.last_trace.last_normalize_info)

def load_weather_stations_to_bq():
    bucket_url = "gs://aemet-weather-data-bucket/weather_stations"
    load_data_to_bq(bucket_url, "load_bq_weather_stations", "weather_stations")

def load_climatic_values_to_bq():
    bucket_url = "gs://aemet-weather-data-bucket/climatic_values"
    load_data_to_bq(bucket_url, "load_bq_climatic_values", "climatic_values", partition_field="ano")

load_weather_stations_to_bq()
load_climatic_values_to_bq()