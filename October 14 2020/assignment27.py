#Name: Jackie Yee
#Date: 14 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 27
                
#Import libraries.
import pandas as pd

#Read in the csv file.
rain = pd.read_csv('AustraliaRain.csv')

#Group the data by location averages.
alburyAvg = rain.groupby(['Location']).get_group('Albury').mean()

#Print the average rainfall at each location.
print(alburyAvg['Rainfall'])
