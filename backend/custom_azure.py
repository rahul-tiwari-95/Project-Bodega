from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'bdgdaostorage' #Azure Blob Storage name
    account_key = '6vYZVHMx6RyHkelHJtPzufT+TWFrX8lg3Abxci8pQDzq1RUcPHCQMB54vKZIfYfapl+uRZzHRB0VpHD+RwNoqA=='
    azure_container = 'media'
    expiration_secs = None
    


class AzureStaticStorage(AzureStorage):
    account_name = 'bdgdaostorage'
    account_key = '6vYZVHMx6RyHkelHJtPzufT+TWFrX8lg3Abxci8pQDzq1RUcPHCQMB54vKZIfYfapl+uRZzHRB0VpHD+RwNoqA=='
    azure_container = 'static'
    expiration_secs = None
