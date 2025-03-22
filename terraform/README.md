# Terraform

## Key Terraform Commands
1. **`terraform init`**: Initializes the Terraform project and downloads the required providers.
2. **`terraform plan`**: Previews the changes Terraform will apply.
3. **`terraform apply`**: Executes the plan and applies the changes defined in the configuration files.
4. **`terraform destroy`**: Removes all resources defined in the configuration files.

### Additional Commands
- **Format Terraform files:**
  ```bash
  terraform fmt
  ```

## Using Terraform with Google Cloud Platform
### Authentication
1. Authenticate with Google Cloud:
   ```bash
   gcloud auth application-default login
   ```
2. Set the `GOOGLE_APPLICATION_CREDENTIALS` environment variable to the path of your service account key file:
   ```bash
   export GOOGLE_APPLICATION_CREDENTIALS="/path/to/your/key.json"
   ```

### Example:
```bash
terraform plan -var="project=XXXXXXXX-XXXXXX"
terraform apply -var="project=XXXXXXXX-XXXXXX"
terraform destroy -var="project=XXXXXXXX-XXXXXX"
```

### Check data types
```sql
CREATE EXTERNAL TABLE `weather_dataset.test`
OPTIONS (
  format = 'PARQUET',
  uris = ['gs://aemet-weather-data-bucket/climatic_values/climatic_values/*.parquet']
);

select * from `weather_dataset.test` where indicativo ='2755X' and fecha = '2024-01-01';


SELECT column_name, data_type 
FROM `weather_dataset.INFORMATION_SCHEMA.COLUMNS`
WHERE table_name = 'test';

```