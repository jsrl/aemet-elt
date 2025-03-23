## Introduction to dlt

[dlt](https://dlthub.com/) is an open-source Python library designed to simplify the process of loading data from various sources into well-structured, live datasets. It offers a user-friendly interface for extracting data from REST APIs, SQL databases, cloud storage, Python data structures, and more.

Key features of `dlt` include:

- **Automatic Schema Inference**: `dlt` automatically infers schemas and data types, normalizes data, and handles complex, nested data structures with ease.
- **Flexible Destination Support**: It supports a wide range of popular destinations for data loading and allows you to create custom destinations, enabling reverse ETL workflows.
- **Scalability**: `dlt` is designed to scale across different environments, from local machines to cloud platforms. It can be deployed wherever Python runs, including on Airflow, serverless functions, or other cloud services.
- **Pipeline Maintenance Automation**: It automates pipeline maintenance by supporting schema evolution, schema contracts, and data contracts, ensuring that your data pipelines remain robust and adaptable over time.

## Data Loading Tool Scripts

- **In Kestra**: The `autodetect_schema` option is set to `True`, which allows Kestra to automatically infer the schema during execution.
  
- **In These Scripts**: The `autodetect_schema` is set to `False`. Instead, we define the schema manually using `dlt/schemas/input` in the pipeline.  
  - On the first execution, you need to copy the output columns into the input schema.  
  - After this initial execution, you can apply any necessary changes to the schema as needed.

- **Existing BigQuery Tables**: BigQuery tables will not automatically change data types if the input schema changes. This means that once a schema is set for a table, you will need to handle any data type adjustments manually if your input schema evolves.

## Python Environment Setup (Local Execution)

To set up the Python environment for local execution, follow these steps:
```sh
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```