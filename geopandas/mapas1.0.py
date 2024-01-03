import geopandas as gpd
import os
import pandas as pd


# Ruta al directorio que contiene los archivos SHP
directorio_shp = 'C:/Users/caroc/Untitled Folder/geopandas/shapes/COMPLETO'

# Obtén la lista de archivos SHP en el directorio
archivos_shp = [archivo for archivo in os.listdir(directorio_shp) if archivo.endswith('.shp')]

# Inicializa una lista para almacenar los GeoDataFrames
gdfs = []

# Ciclo para leer cada archivo SHP
for archivo_shp in archivos_shp:
    # Construye la ruta completa al archivo SHP
    ruta_completa = os.path.join(directorio_shp, archivo_shp)
    
    # Lee el archivo SHP y agrega el GeoDataFrame a la lista
    gdf = gpd.read_file(ruta_completa)
    gdfs.append(gdf)

# Concatena todos los GeoDataFrames en uno solo
resultado_final = gpd.GeoDataFrame(pd.concat(gdfs, ignore_index=True))

# Muestra el GeoDataFrame resultante
print(resultado_final)
