import os
import zipfile
import requests

def download_data(url, name,path='data'):
    if not os.path.exists(path):
        os.mkdir(path)

    response = requests.get(url)
    with open(os.path.join(path, name), 'wb') as f:
        f.write(response.content)

    z = zipfile.ZipFile(os.path.join(path, 'vehicles.zip'))
    z.extractall(path)
VEHICLES = 'http://bit.ly/ddl-cars'
download_data(VEHICLES, 'vehicles.zip')
