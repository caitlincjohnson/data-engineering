resource "aws_instance" "web_server" {
  ami             = "ami-0f1a5f5ada0e7da53"
  instance_type   = "t2.micro"
  security_groups = [module.sg.sg_name]
  user_data       = file("./web/server-script.sh")

  tags = {
    Name = "Web Server"
  }
}

module "eip" {
  source = "../eip"
  instance_id = aws_instance.web_server.id
}

module "sg" {
  source = "../sg"

}

output "instance_id" {
  value = aws_instance.web_server.id
}

output "public_ip" {
  value = module.eip.PublicIP
}