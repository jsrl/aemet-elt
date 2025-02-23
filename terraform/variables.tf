variable "credentials" {
  description = "GCP Credentials"
  default     = "../keys/creds.json"
}

variable "project" {
  description = "Project"
  default     = "<Your Project ID>"
}

variable "region" {
  description = "Region"
  default = "us-central1"
}

variable "location" {
  description = "Project Location"
  default = "US"
}

variable "bq_dataset_weather" {
  description = "Weather dataset"
  default = "weather_dataset"
}

variable "bq_dataset_dbt" {
  description = "Dbt dataset"
  default = "dbt_dataset"
}

variable "gcs_bucket_name" {
  description = "Storage bucket name"
  default = "aemet-weather-data-bucket"
}

variable "gcs_storage_class" {
  description = "Bucket Storage Class"
  default     = "STANDARD"
}
