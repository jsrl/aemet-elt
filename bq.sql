CREATE EXTERNAL TABLE `dlt.dlt_test`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://taxis-bucket-448121-i4/test-dlt/test_dlt/api_data/api_aemet.parquet']
);

select count(*) from `dlt.dlt_test`;