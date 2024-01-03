import zipfile
import os
import pandas as pd
import geopandas as gpd
from shapely.geometry import Point



origen = "C:/Users/caroc/Untitled Folder/geopandas/shapes"  #ruta de los archivos eztraidos
salida = "C:/Users/caroc/Untitled Folder/geopandas/shapes/COMPLETO"   #ruta de los archivos shapes realizados
puntos = gpd.read_file("C:/Users/caroc/Untitled Folder/geopandas",enconding = "utf-8")



for origen in os.listdir(origen):
    for i in range(2010,2022):
        for j in range(1,13):
            if j<10:
                nombrezip = "nadm-{}0{}".format(i,j)
            else:
                nombrezip = "nadm-{}{}".format(i,j)
            if not os.path.exists(os.path.join(origen,nombrezip)):
                continue

            seq0 = gpd.read_file(os.path.join(origen,nombrezip,"nadm_d0.shp"))
            seq1 = gpd.read_file(os.path.join(origen,nombrezip,"nadm_d1.shp"))
            seq2 = gpd.read_file(os.path.join(origen,nombrezip,"nadm_d2.shp"))
            seq3 = gpd.read_file(os.path.join(origen,nombrezip,"nadm_d3.shp"))
            seq4 = gpd.read_file(os.path.join(origen,nombrezip,"nadm_d4.shp"))
            seq0_path = os.path.join(origen, nombrezip, "nadm_d0.shp")
            seq1_path = os.path.join(origen, nombrezip, "nadm_d1.shp")
            seq2_path = os.path.join(origen, nombrezip, "nadm_d2.shp")
            seq3_path = os.path.join(origen, nombrezip, "nadm_d3.shp")
            seq4_path = os.path.join(origen, nombrezip, "nadm_d4.shp")

            if not os.path.exists(seq0_path) or not os.path.isfile(seq0_path):
                print(f"Error: El archivo {seq0_path} no existe o no es un archivo shapefile válido.")
                continue
        
            result0 = gpd.sjoin(puntos,seq0, op = 'intersects')
            result1 = gpd.sjoin(puntos,seq1, op = 'intersects')
            result2 = gpd.sjoin(puntos,seq2, op = 'intersects')
            result3 = gpd.sjoin(puntos,seq3, op = 'intersects')
            result4 = gpd.sjoin(puntos,seq4, op = 'intersects')

            del result0['index_right']
            del result1['index_right']
            del result2['index_right']
            del result3['index_right']
            del result4['index_right']
            del result0['Id']
            del result1['Id']
            del result2['Id']
            del result3['Id']
            del result4['Id']

            result0['categoria'] = 0
            result1['categoria'] = 1
            result2['categoria'] = 2
            result3['categoria'] = 3
            result4['categoria'] = 4
            sequia = sequia.append(result0,ignore_index = True)
            sequia = sequia.append(result1,ignore_index = True)
            sequia = sequia.append(result2,ignore_index = True)
            sequia = sequia.append(result3,ignore_index = True)
            sequia = sequia.append(result4,ignore_index = True)

            seq_finales = sequia.groupby(['lats','lons'])['categoria'].max().reset_index()

            geometry = [Point(xy) for xy in zip (sequia['lons'],sequia['lats'])]
            gdf_seq_finales = gpd.GeoDataFrame(seq_finales,geometry = geometry)

            carpeta_nombrezip = os.path.join(salida,nombrezip)
            if not os.path.exists(carpeta_nombrezip):
                os.mkdir(carpeta_nombrezip)
