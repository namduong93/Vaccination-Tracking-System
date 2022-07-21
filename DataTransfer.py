import requests
import hashlib
import datetime

url = r"https://vac.sp9konin.pl"

def calToken():
    """
Calculate the corresponding token

Use md5 algorithm which encryptes the poly + date to prove the client identity

=========
Parameter
    None

=========
Return
    String
        token
    """
    date = 'poly' + datetime.date.today().strftime(r"%Y-%m-%d")
    return hashlib.md5(date.encode('UTF-8')).hexdigest()

def uploadData(filepath, type):
    """
Upload the datafile or auth data

Use post request to upload the file, following the api from the server

=========
Parameter
    String - filepath
        the path of the file which will be uploaded
    String - type
        the type of the file which will be uploaded, 'data' -> data file, 'auth' -> auth file

=========
Return
    None

    """

    files = {
        "file": ("data.zip", open(filepath, mode="rb"))
    }
    data = {
        "token": calToken(),
        "type": type
    }
    requests.post(url = url, files = files, data = data)
    print(f"[DataTransfer]: UploadData({filepath}, {type})")

def getData(filename):
    """
Download the data from the server

=========
Parameter
    String - filename
        the path of the file which will be download, data.data -> data file, auth.data -> auth file
=========
Return
    None
    """
    file_url = url + "/" + filename
    r = requests.get(file_url)
    with open(filename, "wb") as f:
        f.write(r.content)
    print(f"[DataTransfer]: getData({filename})")
    