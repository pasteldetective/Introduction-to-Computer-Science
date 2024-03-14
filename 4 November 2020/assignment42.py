#Name: Jackie Yee
#Date: 21 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 43

import folium

fileCSV = input("Enter CSV file name:")
outputFile = input("Enter output file")

mapCUNY = folium.Map(location=[40.75, -74.125])

for index,row in fileCSV.iterrows():
    lat = row["LATITUDE"]
    lon = row["LONGITUDE"]
    name = row["Campus"]
    newMarker = folium.Marker([lat, lon], popup=TIME,tiles="Cartodb Positron")
    newMarker.add_to(mapCUNY)

folium.Marker(location = [40.76831, -73.964915], popup = "Hunter College").add_to(mapCUNY)

mapCUNY.save(outfile=outputFile)
