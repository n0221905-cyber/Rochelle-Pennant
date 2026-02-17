import boto3  # AWS
from azure.storage.blob import BlobServiceClient  # Azure
from google.cloud import storage  # GCP

class CloudConnector:
    def __init__(self, provider, **kwargs):
        self.provider = provider.lower()
        if self.provider == 'aws':
            self.s3_client = boto3.client('s3',
                aws_access_key_id=kwargs['aws_access_key_id'],
                aws_secret_access_key=kwargs['aws_secret_access_key'],
                region_name=kwargs.get('region', 'us-east-1'))
        elif self.provider == 'gcp':
            self.gcp_client = storage.Client()
        elif self.provider == 'azure':
            self.blob_service_client = BlobServiceClient.from_connection_string(kwargs['connection_string'])
        else:
            raise ValueError("Unsupported cloud provider")

    def list_buckets(self):
        if self.provider == 'aws':
            return self.s3_client.list_buckets()
        elif self.provider == 'gcp':
            return self.gcp_client.list_buckets()
        elif self.provider == 'azure':
            return self.blob_service_client.list_containers()

    def upload_file(self, file_name, bucket_name):
        if self.provider == 'aws':
            self.s3_client.upload_file(file_name, bucket_name, file_name)
        elif self.provider == 'gcp':
            bucket = self.gcp_client.get_bucket(bucket_name)
            blob = bucket.blob(file_name)
            blob.upload_from_filename(file_name)
        elif self.provider == 'azure':
            blob_client = self.blob_service_client.get_blob_client(container=bucket_name, blob=file_name)
            with open(file_name, "rb") as data:
                blob_client.upload_blob(data)

    def download_file(self, file_name, bucket_name):
        if self.provider == 'aws':
            self.s3_client.download_file(bucket_name, file_name, file_name)
        elif self.provider == 'gcp':
            bucket = self.gcp_client.get_bucket(bucket_name)
            blob = bucket.blob(file_name)
            blob.download_to_filename(file_name)
        elif self.provider == 'azure':
            blob_client = self.blob_service_client.get_blob_client(container=bucket_name, blob=file_name)
            with open(file_name, "wb") as download_file:
                download_file.write(blob_client.download_blob().readall())
