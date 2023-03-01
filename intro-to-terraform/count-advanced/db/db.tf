variable "server_names" {
  type = list(string)
}

resource "aws_instance" "db_server" {
  ami           = "ami-0f1a5f5ada0e7da53"
  instance_type = "t2.micro"
  count = length(var.server_names)
  tags = {
    Name = var.server_names[count.index]
  }
}

output "PrivateIP" {
  value = aws_instance.db_server.*.private_ip
}