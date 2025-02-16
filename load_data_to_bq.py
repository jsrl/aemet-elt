from dlt.sources.filesystem import filesystem, readers
import dlt
import os

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "keys/creds.json"

def load_weather_stations_to_bq():
    bucket_url = "gs://taxis-bucket-448121-i4/weather_stations"

    pipeline = dlt.pipeline(
        pipeline_name='load_bq_weather_stations',
        destination='bigquery', 
        dataset_name='dlt',
    )

    parquet_reader = readers(bucket_url, file_glob="**/*.parquet").read_parquet()
    load_info = pipeline.run(parquet_reader.with_name("weather_stations"),write_disposition="replace")
    print(load_info)
    print(pipeline.last_trace.last_normalize_info)

def load_climatic_values_to_bq():
    bucket_url = "gs://taxis-bucket-448121-i4/climatic_values"

    pipeline = dlt.pipeline(
        pipeline_name='load_bq_climatic_values',
        destination='bigquery', 
        dataset_name='dlt',
    )

    parquet_reader = readers(bucket_url, file_glob="**/*.parquet").read_parquet()
    load_info = pipeline.run(parquet_reader.with_name("climatic_values"),write_disposition="replace")
    print(load_info)
    print(pipeline.last_trace.last_normalize_info)

# Call the functions
load_weather_stations_to_bq()
load_climatic_values_to_bq()