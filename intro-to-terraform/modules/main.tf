provider "aws" {
  region = "us-west-2"
}

module "ec2_module" {
  source = "./ec2"
  ec2_name = "Module EC2"
}

output "module_output" {
  value = module.ec2_module.instance_id
}