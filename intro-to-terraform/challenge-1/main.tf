provider "aws" {
  region = "us-west-2"
}

resource "aws_vpc" "challenge1vpc" {
  cidr_block = "192.168.0.0/24"

  tags = {
    "Name" = var.vpc_name
  }
}

variable "vpc_name" {
  type    = string
  default = "TerraformVPC"
}