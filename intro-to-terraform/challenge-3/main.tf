provider "aws" {
  region = "us-west-2"
}

module "db" {
  source = "./db"
}

module "web" {
  source = "./web"
}

output "PublicIP" {
  value = module.web.public_ip
}

output "PrivateIP" {
  value = module.db.PrivateIP
}