## Auto generated providers.tf ##
## Updated on: 2024-11-27 11:30:27 ##

provider "aws" {
  region = "{region}"
}

provider "aws" {
  alias  = "event-source-account"
  region = "{region}"
  assume_role {
    role_arn = "arn:aws:iam::{account_id}:role/{role_name}"
  }
}
