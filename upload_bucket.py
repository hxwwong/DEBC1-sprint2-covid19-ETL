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

# Upload DOH data & cleanout datadrop/files
base_path2 = "/home/sprint2-covid-project/datadrop/files"

# checks if files consist of more than 1 file/folder, if less than 1, it means no file needed to upload  
if len(os.listdir(f"{base_path2}")) > 1:
    csvs2 = os.listdir(base_path2)
    for csv in csvs2:
        files = f"{base_path2}/{csv}"
        if csv == "case-info-full.csv":
            doh_file = f"{base_path2}/{csv}"
            upload_to_bucket("case-info-full.csv",doh_file, bucket_name)
            os.remove(doh_file)
            print(f"{doh_file} has been uploaded")
        else:
            if files.isfile():
                os.remove(files)
            else:
                pass
else: pass

