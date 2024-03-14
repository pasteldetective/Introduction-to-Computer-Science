#Name: Jackie Yee
#Date: 14 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 30
                

import pandas as pd

aresponse = input("Enter file name:")
bresponse = input("Enter name of the column (Temperature, Luminosity, Radius or Absolute Magnitude) you would like to average:")
pop = pd.read_csv(aresponse)
groupAvg = pop.groupby('Star type').mean()

print("The average", bresponse, "for each Star type is:")
print(groupAvg[bresponse])
