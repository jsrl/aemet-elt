# AEMET ELT

![AEMET ELT](images/aemetelt.gif)

## Prerequisites

Ensure you have the following installed and configured:

- A Google Cloud Project with a Service Account and its associated key.
- Docker Desktop  
- Python (recommended: latest stable version)

## Terraform Setup
```sh
cd terraform
terraform init
terraform plan -var="project=projectId"
terraform apply -var="project=projectId"
```
Expected outputs:
```sh
Terraform has been successfully initialized!

Plan: 3 to add, 0 to change, 0 to destroy.

Apply complete! Resources: 3 added, 0 changed, 0 destroyed.
```

## Start Kestra with Docker
Navigate to the Kestra directory and start the service:
```sh
cd ../ketra
docker compose up -d
```
Once running, Kestra should be accessible at http://localhost:8080.

## Python Environment Setup
```sh
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

