resource "aws_instance" "db_server" {
  ami           = "ami-0f1a5f5ada0e7da53"
  instance_type = "t2.micro"

  tags = {
    Name = "DB Server"
  }
}

output "PrivateIP" {
  value = aws_instance.db_server.private_ip
}