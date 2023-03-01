terraform {
  backend "s3" {
    key    = "terraform/tfstate.tfstate"
    bucket = "s3-bucket-name"
    region = "us-west-2"
  }
}