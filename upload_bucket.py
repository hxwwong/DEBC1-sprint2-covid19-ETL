#!/usr/bin/python3
import os
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] =  r'/home/bonojoves/config/creds.json'

storage_client = storage.Client()


def upload_to_bucket(blob_name, file_path, bucket_name):
    '''
    Upload file to a bucket
    : blob_name  (str) - object name
    : file_path (str)
    : bucket_name (str)
    '''
    bucket = storage_client.get_bucket(bucket_name)
    blob = bucket.blob(blob_name)
    blob.upload_from_filename(file_path)
    return blob

bucket_name = "sprint2-1d"
base_path = "/home/bonojoves/data"

csvs = os.listdir(base_path)
# print(csvs)

for csv in csvs:
    filename = f"{base_path}/{csv}"
    upload_to_bucket(csv,filename, bucket_name)
    os.remove(filename)
    print(f"{filename} has been uploaded")
