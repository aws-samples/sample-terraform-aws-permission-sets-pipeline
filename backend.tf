## Auto generated providers.tf ##
## Updated on: 2024-11-27 11:30:27 ##

terraform {
  required_version = ">=1.6"
  backend "s3" {
    region         = "{region}"
    bucket         = "{bucket_name}"
    key            = "terraform.tfstate"
    dynamodb_table = "{table_name}"
    encrypt        = "true"
  }
}
