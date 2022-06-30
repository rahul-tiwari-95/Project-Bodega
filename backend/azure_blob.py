from storages.backends.azure_storage import AzureStorage

class AzureMediaStorage(AzureStorage):
    account_name = 'projectbodegadb'
    account_key = 'oPxyq+14Ob7BGY2fkSKsEQPiObqqUPfS+s1zvKd4jUdLb1UZ+XzC5Lg4p2WVGgeUjDF5A2wNpPqO+AStDGmBJw=='
    azure_container ='media'
    expiration_secs = None
    
    

class AzureStaticStorage(AzureStorage):
    account_name = 'projectbodegadb'
    account_key = 'oPxyq+14Ob7BGY2fkSKsEQPiObqqUPfS+s1zvKd4jUdLb1UZ+XzC5Lg4p2WVGgeUjDF5A2wNpPqO+AStDGmBJw=='
    azure_container ='static'
    expiration_secs = None
    
