RESOURCE_GROUP_NAME=Azuredevops
STORAGE_ACCOUNT_NAME=tfstateloihh1
CONTAINER_NAME=tfstate
az storage account create --resource-group Azuredevops --name tfstateloihh1 --sku Standard_LRS --encryption-services blob
az storage container create --name tfstate --account-name tfstateloihh1
echo $(az storage account keys list --resource-group Azuredevops --account-name tfstateloihh1 --query '[0].value' -o tsv)
