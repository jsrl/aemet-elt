# AEMET ELT

![AEMET ELT](images/aemetelt.gif)

## Table of Contents
1. [Problem statement](#problem-statement)
2. [Project solution](#project-solution)
3. [Tech Stack](#tech-stack)
4. [Prerequisites](#prerequisites)
5. [Datasets](#datasets)
6. [Usage](#usage)
7. [Orchestration](#orchestration)
8. [Visualization](#visualization)

## Problem Statement

Spain has over 900 meteorological stations across the country that collect valuable weather data. However, accessing and processing this data in a structured manner can be a challenging task, especially when trying to analyze it over different time periods or extract meaningful statistics from it.

## Project Solution

This project leverages the open data APIs provided by [AEMET (Agencia Estatal de Meteorología)](https://opendata.aemet.es/dist/index.html) to collect historical weather data from over 900 meteorological stations in Spain. The system gathers data on a yearly basis and processes it to generate detailed statistics on weather measurements (e.g., temperature, humidity, etc.) and the geographical locations of the stations. This approach allows users to easily analyze weather trends, compare station data, and gain insights into the meteorological conditions across the country.

## Tech Stack

- **Google Cloud Platform**: Cloud infrastructure.
- **Docker**: Containerization.
- **Terraform**: Infrastructure as Code.
- **Google Cloud Storage**: Storage.
- **BigQuery**: Data Warehouse.
- **Kestra**: Orchestration.
- **dlt**: Data Loading tool.
- **dbt**: Data Transformation tool.
- **Looker Studio**: Data visualization.


## Prerequisites

Ensure you have the following installed and configured:

- A Google Cloud Project with a Service Account and its associated key.
- Docker Desktop
- Terraform

## Datasets

AEMET (Agencia Estatal de Meteorología) provides a set of open data APIs that allow users to access meteorological data for Spain. These APIs provide valuable information, including climate values and weather station data. 

You can obtain an API key for free by registering at the following link:  
[Get your free API Key](https://opendata.aemet.es/centrodedescargas/altaUsuario)

### API Metadata

- **Climate Values**:  
  Metadata for the Climate Values API can be found here:  
  [Climate Values Metadata](https://opendata.aemet.es/opendata/sh/b3aa9d28)

- **Weather Stations**:  
  Metadata for the Weather Stations API can be found here:  
  [Weather Stations Metadata](https://opendata.aemet.es/opendata/sh/0556af7a)

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



