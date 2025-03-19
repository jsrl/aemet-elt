CREATE EXTERNAL TABLE `weather_dataset.test`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://aemet-weather-data-bucket/climatic_values/climatic_values/*.parquet']
);

select * from `weather_dataset.test` where indicativo ='2755X' and fecha = '2024-01-01';


SELECT column_name, data_type 
FROM `weather_dataset.INFORMATION_SCHEMA.COLUMNS`
WHERE table_name = 'test';