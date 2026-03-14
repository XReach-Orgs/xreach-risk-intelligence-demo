locals {
  project_name = var.project_name
  environment  = var.environment
  location     = var.location

  common_tags = {
    project     = local.project_name
    environment = local.environment
    managed_by  = "terraform"
    platform    = "xreach-risk-intelligence"
  }

  name_prefix = "${local.project_name}-${local.environment}"
}

module "resource_group" {
  source = "../../modules/resource_group"

  name     = "${local.name_prefix}-rg"
  location = local.location
  tags     = local.common_tags
}

module "log_analytics" {
  source = "../../modules/log_analytics"

  name                = "${local.name_prefix}-law"
  location            = local.location
  resource_group_name = module.resource_group.name
  tags                = local.common_tags
}

module "network" {
  source = "../../modules/network"

  resource_group_name = module.resource_group.name
  location            = local.location
  vnet_name           = "${local.name_prefix}-vnet"
  vnet_address_space  = var.vnet_address_space

  aks_subnet_name           = "${local.name_prefix}-aks-subnet"
  aks_subnet_address_prefix = var.aks_subnet_address_prefix

  tags = local.common_tags
}

module "acr" {
  source = "../../modules/acr"

  name                = var.acr_name
  location            = local.location
  resource_group_name = module.resource_group.name
  sku                 = var.acr_sku
  admin_enabled       = var.acr_admin_enabled
  tags                = local.common_tags
}

module "key_vault" {
  source = "../../modules/key_vault"

  name                        = var.key_vault_name
  location                    = local.location
  resource_group_name         = module.resource_group.name
  tenant_id                   = var.tenant_id
  sku_name                    = var.key_vault_sku_name
  purge_protection_enabled    = var.key_vault_purge_protection_enabled
  soft_delete_retention_days  = var.key_vault_soft_delete_retention_days
  tags                        = local.common_tags
}

module "aks" {
  source = "../../modules/aks"

  cluster_name              = "${local.name_prefix}-aks"
  location                  = local.location
  resource_group_name       = module.resource_group.name
  dns_prefix                = "${local.name_prefix}-dns"
  kubernetes_version        = var.kubernetes_version

  default_node_pool_name    = var.default_node_pool_name
  default_node_count        = var.default_node_count
  vm_size                   = var.default_node_vm_size
  subnet_id                 = module.network.aks_subnet_id

  acr_id                    = module.acr.id
  log_analytics_workspace_id = module.log_analytics.workspace_id

  enable_workload_identity  = var.enable_workload_identity
  enable_oidc_issuer        = var.enable_oidc_issuer

  tags = local.common_tags
}