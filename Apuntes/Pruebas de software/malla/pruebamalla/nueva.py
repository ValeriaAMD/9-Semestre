import requests
from bs4 import BeautifulSoup

url = "https://www.ncei.noaa.gov/pub/data/nidis/shapefiles/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

for anio in range(2010, 2024):
    string = 'nadm-{}'.format(anio)
    file_name = f"{string}.zip"
    file_url = None

for mes in range(1,13):
    string = 'nadm-{}'.format(mes)
    file_name = f"{string}.zip"
    file_url = None

    for link in soup.find_all('a', href=True):
        if string in link['href']:
            file_url = url + link['href']
            break

    if file_url:
        r = requests.get(file_url, stream=True)
        with open(file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=8192):
                if chunk:
                    f.write(chunk)
        print(f"Descarga de {file_name} completa.")

    else:
        print(f"No se encontró el archivo para {anio}.")
