#Name: Jackie Yee
#Date: 21 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 36

import pandas as pd

csvFile = input('Enter CSV file name: ')         #Name of the CSV file
tickets = pd.read_csv(csvFile)     #Read in the file to a dataframe
print("The 10 worst offenders are:")
print(tickets["Plate ID"].value_counts()[:10]) #Print out the dataframe			#Print out the dataframe
