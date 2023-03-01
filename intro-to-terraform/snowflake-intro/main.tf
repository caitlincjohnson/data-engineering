

# terraform {
#   required_providers {
#     snowflake = {
#       source  = "Snowflake-Labs/snowflake"
#       version = "~> 0.35"
#     }
#   }
# }

# provider "snowflake" {
#   role   = "SECURITYADMIN"
#   region = "us-west-2"
#   alias  = "security_admin"
# }

# resource "snowflake_database" "terraform_db" {
#   name = "TERRAFORM"
# }

# resource "snowflake_warehouse" "terraform_wh" {
#   name                                = "TERRAFORM_WH"
#   warehouse_size                      = "XSMALL"
#   auto_suspend                        = 15
#   enable_query_acceleration           = false
#   query_acceleration_max_scale_factor = 0
#   max_concurrency_level               = 2
# }

# resource "snowflake_role" "terraform_svc_role" {
#   provider = snowflake.security_admin
#   name     = "TERRAFORM_SVC_ROLE"
# }

# resource "snowflake_database_grant" "terraform_svc_role_db_grant" {
#   provider          = snowflake.security_admin
#   database_name     = snowflake_database.terraform_db.name
#   privilege         = "USAGE"
#   roles             = [snowflake_role.terraform_svc_role.name]
#   with_grant_option = false
# }

# resource "snowflake_schema" "terraform_metadata" {
#   database   = snowflake_database.terraform_db.name
#   name       = "METADATA"
#   is_managed = false
# }

# resource "snowflake_schema_grant" "terraform_metadata_schema_grant" {
#   provider          = snowflake.security_admin
#   database_name     = snowflake_database.terraform_db.name
#   schema_name       = snowflake_schema.terraform_metadata.name
#   privilege         = "USAGE"
#   roles             = [snowflake_role.terraform_svc_role.name]
#   with_grant_option = false
# }

# resource "snowflake_warehouse_grant" "terraform_svc_role_terraform_wh" {
#   provider          = snowflake.security_admin
#   warehouse_name    = snowflake_warehouse.terraform_wh.name
#   privilege         = "USAGE"
#   roles             = [snowflake_role.terraform_svc_role.name]
#   with_grant_option = false
# }

# resource "snowflake_user" "demo_user" {
#   provider          = snowflake.security_admin
#   name              = "DEMO_USER"
#   default_warehouse = snowflake_warehouse.terraform_wh.name
#   default_role      = snowflake_role.terraform_svc_role.name
#   default_namespace = "${snowflake_database.terraform_db.name}.${snowflake_schema.terraform_metadata.name}"
# }

# resource "snowflake_role_grants" "grants" {
#   provider  = snowflake.security_admin
#   role_name = snowflake_role.terraform_svc_role.name
#   users     = [snowflake_user.demo_user.name]
# }