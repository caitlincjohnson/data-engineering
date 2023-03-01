provider "aws" {
  region = "us-west-2"
}

resource "aws_instance" "ec2" {
  ami           = "ami-0f1a5f5ada0e7da53"
  instance_type = "t2.micro"
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

  ingress = [ {
    cidr_blocks = [ "0.0.0.0/0" ]
    from_port = 443
    protocol = "TCP"
    to_port = 443
  } ]

  egress = [ {
    cidr_blocks = [ "0.0.0.0/0" ]
    from_port = 443
    protocol = "TCP"
    to_port = 443
  } ]
}

output "eip" {
  value = aws_eip.eip_demo.public_ip
}