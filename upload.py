import requests
import json

url = "https://share.streamlit.io/api/v1/deploy"



headers = {
  'User-Agent': "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/127.0.0.0 Safari/537.36",
  'Content-Type': "application/json",
  'x-csrf-token': "Q3hoTUlSbDZ3aTMxbzVHblNYNmdGcXcyNzhHWjJpSje/Tgk0a+KaNdl0f7P0UuWrUK6m3rCblAJvq5MYIGYA+g==",
  'Cookie': "streamlit_session=MTcyMTIyMDQ5Mnx0Z3JnX3drLW95SFY2djRYUklfNzNrODN3ZFlKcDBlY1JhMVljQVlvUHdDNnc5TkhVYVpOWjhFY2pWTXhlNEZmMnBSdVFwS0M1SzRMc0szS1VWRW1YSmw5U1g2TzVZTzZya0puN1Z0RFh3MF8yZDdEQjF4cW5uNWMtU25rTHFGNW1CY2xDZUd3bFNlWEdwNVZLa2F4NlRRWDBtN1VGc2ZKNXFiTVdleEZoMzFOeFE3alJqX01uWVRDZlE9PXyzOJ4ofMbzdbXHjbaQM3ENLaNVErUtffc9cq5MkXxKOA==; _streamlit_csrf=MTcyMjMxNTgxM3xJaTlFV21obFUwdDNPV2RQZFVoVmVVTnRNbVZwZUZGUU1tdE1iakkyZFUxM1YwcFFWVkZvU1ZCVGN6QTlJZ289fDY5LsQ6lZopUfhYcT8HIj-5lkr1MxlNQUTdYze6hiOe"
}
import os

def get_files_starting_with(folder_path, prefix):

  files = []
  for filename in os.listdir(folder_path):
    if filename.startswith(prefix):
      files.append(filename)
      #files.append(os.path.join(folder_path, filename))

  return files


folder_path = os.getcwd()# Replace with your folder path
prefix = "main"

files = get_files_starting_with(folder_path, prefix)

for file in files:
    payload = json.dumps({
      "repository": "https://github.com/kinshusharma0412/ccc",
      "branch": "main",
      "secrets": "",
      "mainModule": file,
      "pythonVersion": "311",
      "subdomain": file[:-3],
      "workspaceName": "kinshusharma0412"
    })
    response = requests.post(url, data=payload, headers=headers)
    print(file[:-3])
    print(response.text)