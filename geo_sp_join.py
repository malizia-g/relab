
import geopandas as gpd
import pandas as pd



lombardia = gpd.read_file('R03_11_WGS84.shp')
print(lombardia.head())

cened2 = pd.read_csv('res.csv')
print(cened2.head())

from shapely.geometry import Point 
geometry = [Point(xy) for xy in zip(cened2['lat'], cened2['lng'])]


Cened2crs = {'init': 'epsg:4326'}

cened2GDF = gpd.GeoDataFrame(cened2, crs=Cened2crs, geometry=geometry)
print(cened2GDF.head())

#Convertiamo ora le coordinate dei punti nello stesso sistema di riferimento del dataframe della lombardia. 
cened2GDF = cened2GDF.to_crs({'init': 'epsg:32632'}) 
cened2GDF.head()

#Per poter effettuare la sjoin (cioe' per associare ad un punto - cioe' ad un indirizzo
# - il poligono in cui si trova - cioe' la sezione del censimento in cui si trova) 
#dobbiamo assicurarci che il campo geometry del primo geodataframe sia di tipo POINT 
#mentre quello del secondo geodataframe sia di tipo POLYGON

print(type(cened2GDF.geometry[0])) #Verifico i dati del cened (Point)

print(type(lombardia.geometry[0])) #Verifico i dati istat (Polygon)

#Effettuiamo ora la sjoin
indirizzoSezione = gpd.sjoin(left_df=cened2GDF, right_df=lombardia, how="left", op="intersects")

print(indirizzoSezione.head())

indirizzoSezione.to_csv("res2.csv")