#Import the folium package for making maps
import folium
import pandas as pd

cuny = pd.read_csv('c.csv')
print(cuny["campus"])

