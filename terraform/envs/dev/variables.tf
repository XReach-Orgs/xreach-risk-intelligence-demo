variable "project_name" {}
variable "environment" {}
variable "location" {}

variable "tenant_id" {}

variable "vnet_address_space" {
  type = list(string)
}

variable "aks_subnet_address_prefix" {
  type = list(string)
}

variable "acr_name" {}
variable "acr_sku" {
  default = "Basic"
}
variable "acr_admin_enabled" {
  default = false
}

variable "key_vault_name" {}
variable "key_vault_sku_name" {
  default = "standard"
}
variable "key_vault_purge_protection_enabled" {
  default = true
}
variable "key_vault_soft_delete_retention_days" {
  default = 7
}

variable "kubernetes_version" {}
variable "default_node_pool_name" {
  default = "system"
}
variable "default_node_count" {
  default = 2
}
variable "default_node_vm_size" {
  default = "Standard_DS2_v2"
}

variable "enable_workload_identity" {
  default = true
}
variable "enable_oidc_issuer" {
  default = true
}