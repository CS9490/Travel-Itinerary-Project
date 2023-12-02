terraform {
  backend "s3" {
    bucket = "nawayfarer-ishtiaq-khan"
    key    = "core/terraform.tfstate"
    region = "us-east-2"
  }
}