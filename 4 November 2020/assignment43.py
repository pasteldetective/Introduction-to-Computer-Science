#Name: Jackie Yee
#Date: 21 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 43

import folium
import pandas as pd

fileCSV = input("Enter CSV file name:")
outputFile = input("Enter output file")

cuny = pd.read_csv(fileCSV)

mapCUNY = folium.Map(location=[40.75, -74.125])

for index,row in cuny.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    newMarker = folium.Marker([lat, lon])
    newMarker.add_to(mapCUNY)

mapCUNY.save(outfile=outputFile)
