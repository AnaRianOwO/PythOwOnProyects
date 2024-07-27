from azure.storage.blob import BlobServiceClient

connection_string = "blob:https://ok.ru/e984e26e-c39a-4180-83a6-86d63bcce0c8"
blob_service_client = BlobServiceClient.from_connection_string(connection_string)

container_name = "nombre_del_contenedor"
container_client = blob_service_client.get_container_client(container_name)


blob_name = "nombre_del_archivo_blob"
blob_client = container_client.get_blob_client(blob_name)
with open("peli.mp4", "wb") as file:
    file.write(blob_client.download_blob().readall())


