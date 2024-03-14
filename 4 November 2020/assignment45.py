#Name: Jackie Yee
#Date: 21 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 45

import folium
import pandas as pd

fileCSV = input("Please enter the name of the input file:")
outputFile = input("Please enter the name of the output file:")
defineBor = input("Please enter the name of the borough:")

mapLoca = folium.Map(tiles="Stamen Watercolor")
suffering = pd.read_csv(fileCSV)

df = suffering.groupby("Borough").get_group(defineBor)

for index,row in df.iterrows():
    lat = row["Latitude"]
    lon = row["Longitude"]
    newMarker = folium.Marker([lat, lon], popup=row["Address"])
    newMarker.add_to(mapLoca)

mapLoca.save(outfile=outputFile)
