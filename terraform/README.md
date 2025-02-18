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

