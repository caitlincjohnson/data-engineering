provider "aws" {
  region = "us-west-2"
}

variable "ingressrules" {
  type    = list(number)
  default = [80, 443]
}

variable "egressrules" {
  type    = list(number)
  default = [80, 443, 25, 3306, 53, 8080]
}

resource "aws_instance" "ec2" {
  ami             = "ami-0f1a5f5ada0e7da53"
  instance_type   = "t2.micro"
  security_groups = [aws_security_group.sec_gp_demo.name]

  tags = {
    Name = "EC2 Demo"
  }
}

resource "aws_eip" "eip_demo" {
  instance = aws_instance.ec2.id
}

resource "aws_security_group" "sec_gp_demo" {
  name = "Allow HTTPS"

  dynamic "ingress" {
    iterator = port
    for_each = var.ingressrules
    content {
      cidr_blocks = ["0.0.0.0/0"]
      from_port   = port.value
      protocol    = "TCP"
      to_port     = port.value
    }
  }

  dynamic "egress" {
    iterator = port
    for_each = var.egressrules
    content {
      cidr_blocks = ["0.0.0.0/0"]
      from_port   = port.value
      protocol    = "TCP"
      to_port     = port.value
    }
  }
}

output "eip" {
  value = aws_eip.eip_demo.public_ip
}