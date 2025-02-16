from dlt.sources.filesystem import filesystem, readers
import dlt
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys/creds.json"

def load_data_to_bq(bucket_url, pipeline_name, table_name):
    print(f"Starting load for {table_name}...")
    pipeline = dlt.pipeline(
        pipeline_name=pipeline_name,
        destination="bigquery", 
        dataset_name="dlt",
    )

    parquet_reader = readers(bucket_url, file_glob="**/*.parquet").read_parquet()
    load_info = pipeline.run(parquet_reader.with_name(table_name), write_disposition="replace")
    print(load_info)
    print(pipeline.last_trace.last_normalize_info)

def load_weather_stations_to_bq():
    bucket_url = "gs://taxis-bucket-448121-i4/weather_stations"
    load_data_to_bq(bucket_url, "load_bq_weather_stations", "weather_stations")

def load_climatic_values_to_bq():
    bucket_url = "gs://taxis-bucket-448121-i4/climatic_values"
    load_data_to_bq(bucket_url, "load_bq_climatic_values", "climatic_values")

# Call the functions
load_weather_stations_to_bq()
load_climatic_values_to_bq()