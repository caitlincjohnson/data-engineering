provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "db_server" {
  ami           = "ami-0f1a5f5ada0e7da53"
  instance_type = "t2.micro"

  tags = {
    Name = "DB Server"
  }
}

resource "aws_instance" "web_server" {
  ami             = "ami-0f1a5f5ada0e7da53"
  instance_type   = "t2.micro"
  security_groups = [aws_security_group.web_traffic.name]
  user_data       = file("server-script.sh")

  tags = {
    Name = "Web Server"
  }
}

resource "aws_eip" "web_ip" {
  instance = aws_instance.web_server.id
}

variable "ingress" {
  type    = list(number)
  default = [80, 433]
}

variable "egress" {
  type    = list(number)
  default = [80, 433]
}

resource "aws_security_group" "web_traffic" {
  name = "Allow Web Traffic"

  dynamic "ingress" {
    iterator = port
    for_each = var.ingress
    content {
      from_port   = port.value
      to_port     = port.value
      protocol    = "TCP"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }

  dynamic "egress" {
    iterator = port
    for_each = var.egress
    content {
      from_port   = port.value
      to_port     = port.value
      protocol    = "TCP"
      cidr_blocks = ["0.0.0.0/0"]
    }
  }
}

output "PublicIP" {
  value = aws_eip.web_ip.public_ip
}

output "PrivateIP" {
  value = aws_instance.db_server.private_ip
}