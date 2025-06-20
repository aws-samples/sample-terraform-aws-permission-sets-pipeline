## Auto generated providers.tf ##
## Updated on: 2024-11-27 11:30:27 ##

terraform {
  required_version = ">=1.5"
  backend "s3" {
    region         = "{region}"
    bucket         = "{bucket_name}"
    key            = "{key_name}"
    dynamodb_table = "{table_name}"
    encrypt        = "true"
  }
}
