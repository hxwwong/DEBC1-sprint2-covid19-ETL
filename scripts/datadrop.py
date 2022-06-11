import pandas as pd
import gdown
import glob
import re
import fitz # PyMuPDF
import requests
import os
import io
import pickle
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from googleapiclient.http import MediaIoBaseDownload

def find_url(string):
   #Find all the String that matches with the pattern
   regex = r"https://.*"
   url = re.findall(regex,string)
   for url in url:
      return url

def parse_pdf(file):
    #get bitly link from the pdf file
    with fitz.open(file) as my_pdf_file:

        #loop through every page
        for page_number in range(1,len(my_pdf_file)+1):
            # acess individual page
            page = my_pdf_file[page_number-1]
            text = page.get_text()
            url = find_url(text)
            if url is not None:
                return url

def listFiles(service, folder_id):
    #parameters service: pass google service instance
    # folder_id: file_id of gdrive folder

    listOfFiles = []

    query = f"'{folder_id}' in parents and mimeType='text/csv'"

    # Get list of csv in shared folder
    page_token = None
    while True:
        response = service.files().list(
            q=query,
            fields="nextPageToken, files(id, name)",
            pageToken=page_token,
            includeItemsFromAllDrives=True, 
            supportsAllDrives=True
        ).execute()

        for file in response.get('files', []):
            listOfFiles.append(file)

        page_token = response.get('nextPageToken', None)
        if page_token is None:
            break

    return listOfFiles

def download_files(df,findlist, file_name):
    #download files using gdrive fileid
    # parameters df: pandas dataframe of google drive folder files
    # findlist: string to find in gdrive file name
    # file_name: what you want your file to output as will add number at end    

    idlist = df[df.name.str.contains('|'.join(findlist))]['id']
    file_names = [str(x).zfill(2) for x in range(len(idlist))]
    file_names = ["case-info_"+s for s in file_names]

    print(f"found {len(idlist)} files")
    print("starting file downloads...")

    for ids,file_name in zip(idlist,file_names):
        request = service.files().get_media(fileId=ids)

        fh = io.BytesIO()
        downloader = MediaIoBaseDownload(fd=fh, request=request)

        done = False
        while not done:
            status, done = downloader.next_chunk()
            print('Download progress {0}'.format(status.progress()*100))
        
        #write data to folder
        fh.seek(0)
        with open(f"{file_name}.csv", 'wb') as f:
            f.write(fh.read())
            f.close()
        print(f'{file_name} downloaded')

    print('All file downloads complete')


def get_gdrive_service(cjson):
    SCOPES = ['https://www.googleapis.com/auth/drive.readonly']
    creds = None
    # The file token.pickle stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.pickle'):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                cjson, SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.pickle', 'wb') as token:
            pickle.dump(creds, token)
    # return Google Drive API service
    return build('drive', 'v3', credentials=creds)


#create service instance
client_secret = 'client_secret_file.json'
service = get_gdrive_service(client_secret)
print()


#change directory for easy file cleanup on future iterations
home = os.getcwd()
os.chdir(f"{home}/files")
print(os.getcwd())
folder_id = "1ZPPcVU4M7T-dtRyUceb0pMAd8ickYf8o"
url = "https://drive.google.com/drive/folders/1ZPPcVU4M7T-dtRyUceb0pMAd8ickYf8o"
gdown.download_folder(url, quiet=True, use_cookies=False)

pdffile = glob.glob(r"READ ME FIRST/*.pdf")
print(pdffile)


filename = f"{pdffile}"

datadrop_url = parse_pdf(filename)

download_url = requests.get(datadrop_url).url
print(f"found link: {download_url}")

# extracts the file_id from the url link
file_id = download_url.split('?')[0].split('/')[-1]

files = listFiles(service, file_id)
df = pd.DataFrame(files)

findcaseinfo = ['Case Information']
download_files(df,findcaseinfo,"case-info_")

caseinfo_files = glob.glob("case-info_**.csv")
print(caseinfo_files)

caseinfo = pd.concat(map(pd.read_csv, caseinfo_files))

caseinfo.to_csv('case-info-full.csv',index = False)

