provider "aws" {
  region                      = "us-east-1"
  access_key                  = "test"
  secret_key                  = "test"
  s3_use_path_style            = true

  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_requesting_account_id  = true

  endpoints {
    s3 = "http://localhost:4566"
  }
}

resource "aws_s3_bucket" "equipment_data" {
  bucket = "mining-equipment-monitor-data-tf"
}

resource "aws_s3_bucket" "equipment_logs" {
  bucket = "mining-equipment-monitor-logs"
}