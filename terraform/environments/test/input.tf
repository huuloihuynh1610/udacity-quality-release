# Azure GUIDS
variable "subscription_id" {
    default = ""
}
variable "client_id" {
    default = ""
}
variable "client_secret" {
    default = ""
}
variable "tenant_id" {
    default = ""
}

# Resource Group/Location
variable "location" {
    default = ""
}
variable "resource_group" {
    default = ""
}
variable "application_type" {
    default = ""
}

# Network
variable virtual_network_name {
    default = ""
}
variable address_prefix_test {
    default = "10.5.1.0/24"
}
variable address_space {
    default = ["10.5.0.0/16"]
}

