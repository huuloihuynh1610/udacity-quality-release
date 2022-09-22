# Resource Group
variable resource_group {
    default = ""
}
variable location {
    default = ""
}
# Network
variable virtual_network_name {
    default = ""
}
variable address_space {
    default = ["10.5.0.0/16"]
}
variable "application_type" {
    default = ""
}
variable "resource_type" {
    default = ""
}
variable "address_prefix_test" {
    default = "10.5.1.0/24"
}

