# AEMET ELT

## Pre-requisites

- Google Cloud Project
- Terraform Service Account and associated key

## Terraform Setup

```sh
terraform init
```
Terraform has been successfully initialized!


```sh
terraform plan -var="project=projectId"
```
Plan: 3 to add, 0 to change, 0 to destroy.


```sh
terraform apply -var="project=projectId"
```
Apply complete! Resources: 3 added, 0 changed, 0 destroyed.


## Requisites

- Python

## Python Environment Setup

```sh
python -m venv venv
source venv/Scripts/activate
pip install -r requirements.txt
```

