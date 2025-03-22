# Data Loading Tool Scripts

* In kestra autodetect_schema=True
* In these scripts autodetect_schema=False and we use dlt/schemas/input in the pipeline.
You need to copy the output columns in the input the first execution. Then you can apply changes.

* Existing bq tables won't change the data type after your input changes
