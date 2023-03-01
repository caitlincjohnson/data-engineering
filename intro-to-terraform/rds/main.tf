provider "aws" {
  region = "us-west-2"
}

resource "aws_db_instance" "rds_demo" {
  name                = "rdsDemo"
  identifier          = "rds-demo"
  instance_class      = db.t2.micro
  engine              = "mariadb"
  engine_version      = "10.2.21"
  port                = 3306
  allocated_storage   = 20
  skip_final_snapshot = true
}