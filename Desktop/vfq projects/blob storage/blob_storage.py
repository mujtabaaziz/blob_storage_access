from azure.storage.blob import BlobServiceClient, PublicAccess

# Connection string to your storage account
connection_string = ""
# connection_string = "DefaultEndpointsProtocol=https;AccountName=dlsstagall;AccountKey=GVC9vl+nR44iLO5MyVs/bWkmYXeeEKUG/JhPNIaKhiO5w4iN3WkWXUJEjjrArAOr+Sb/FIuJNN7t+AStuJVGmw==;EndpointSuffix=core.windows.net"

# Create BlobServiceClient object
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

# Name of the container
container_name = ""
# container_name = "cob-customer-stag"

# Get the container client
container_client = blob_service_client.get_container_client(container_name)
container_client.set_container_access_policy(signed_identifiers={}, public_access=PublicAccess.Blob)
# Set public access level
# container_client.set_container_access_policy(public_access=PublicAccess.Blob)

print(f"Public access has been set for the container '{container_name}'")
