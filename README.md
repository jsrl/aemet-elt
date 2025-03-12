# AEMET ELT

## Prerequisites

Ensure you have the following installed and configured:

- A Google Cloud Project  
- A Terraform Service Account with associated key  
- Docker Desktop  
- Python (recommended: latest stable version)

## Terraform Setup

Initialize Terraform: 
```sh
cd terraform
terraform init
```
Run a plan to preview the changes:
```sh
terraform plan -var="project=projectId"
```
Expected output:
```sh
Plan: 3 to add, 0 to change, 0 to destroy.
```

Apply the changes:
```sh
terraform apply -var="project=projectId"
```
Exprected output:
```sh
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

