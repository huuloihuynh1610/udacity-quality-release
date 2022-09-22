# Resource Group/Location
variable "location" {
    default = ""
}
variable "application_type" {
    default = ""
}
variable "resource_type" {
    default = "nsg"
}
variable "resource_group" {
    default = "udacity-project"
}
variable "subnet_id" {
    default = ""
}
variable "address_prefix_test" {
    default = "10.5.1.0/24"
}
