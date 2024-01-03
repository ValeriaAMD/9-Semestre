import requests
from bs4 import BeautifulSoup
import os

url = "https://www.ncei.noaa.gov/pub/data/nidis/shapefiles/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for year in range(2010, 2024):
    for month in range(1, 13):
        string = f"nadm-{year}-{month:02d}.zip"
        file_url = None

        for link in soup.find_all('a', href=True):
            if string in link['href']:
                file_url = url + link['href']
                break

        if file_url:
            try:
                r = requests.get(file_url, stream=True)
                with open(os.path.join(os.getcwd(), string), 'wb') as f:
                    for chunk in r.iter_content(chunk_size=8192):
                        if chunk:
                            f.write(chunk)
                print(f"Descarga de {string} completa.")
            except Exception as e:
                print(f"Error al descargar {string}: {e}")
        else:
            print(f"No se encontró el archivo para {string}.")
