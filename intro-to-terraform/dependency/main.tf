provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "database" {
  ami           = "ami-0f1a5f5ada0e7da53"
  instance_type = "t2.micro"

  tags = {
    Name = "database"
  }
}

resource "aws_instance" "web" {
  ami           = "ami-0f1a5f5ada0e7da53"
  instance_type = "t2.micro"

  tags = {
    Name = "webserver"
  }

  depends_on = [aws_instance.database]
}