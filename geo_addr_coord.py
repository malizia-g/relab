#README:
#impostare la versione 3 di python su gitpod: o rimane impostata???
#Installare le dipendenze: pip3 install -r requirements.txt  o rimangono installate???

import pandas as pd
import geopandas as gpd

cened2 = pd.read_csv("cened/DB_Cened2_100.csv")
print(cened2.head())
print("hello")
#Inserisco campo FullAddress
cened2.insert(26, 'FullAddress', cened2[['INDIRIZZO', 'COMUNE']].apply(lambda x: ' '.join(x), axis = 1) )
print(cened2.head())

from googlemaps import Client as GoogleMaps

gmaps = GoogleMaps('AIzaSyAFlR30N1paHO3FsTgoPOetrw2P1xZV028')
#AIzaSyCzUI8LYmnHPyFrtRT8Q8IEREZfOygUl-U  API WALTER

def getLatLong(row):
  geocode_result = gmaps.geocode(row['FullAddress'])
  row['lat'] = geocode_result[0]['geometry']['location']['lat']
  row['lng'] = geocode_result[0]['geometry']['location']['lng']
  return row

cened2 = cened2.apply(getLatLong, axis=1)
print(cened2.head)

cened2.to_csv("results/res.csv")





