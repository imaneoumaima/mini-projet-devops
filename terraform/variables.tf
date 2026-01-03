variable "region" { default = "us-east-1" }
variable "vpc_cidr" { default = "10.0.0.0/16" }
variable "public_subnet_cidr" { default = "10.0.1.0/24" }
variable "key_name" {}
variable "public_key" {}
variable "instance_type" { default = "t3.micro" }
variable "ami_id" {} # AMI Ubuntu 22.04 dans ta région
