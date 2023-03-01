#!/bin/bash
sudo yum update
sudo yum isntall -y httpd
sudo systemctl start httpd
sudo systemctl enable httpd
each "<h1>Hello from Terraform</h1>" | sudo tee /var/www/html/index.html