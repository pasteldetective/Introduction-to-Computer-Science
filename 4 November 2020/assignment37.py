#Name: Jackie Yee
#Date: 21 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 37

import pandas as pd

fFile = input("Enter file name:")
film = pd.read_csv(fFile)
print("There were", len(film), "film permits.")
print(film["Borough"].value_counts())
print(film["EventType"].value_counts())
