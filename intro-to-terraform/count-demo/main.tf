provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "ec2" {
  ami           = "ami-0f1a5f5ada0e7da53"
  instance_type = "t2.micro"
  count =  3
}