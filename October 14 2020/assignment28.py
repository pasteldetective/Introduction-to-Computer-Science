#Name: Jackie Yee
#Date: 14 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 27
                
import matplotlib.pyplot as plt
import pandas as pd

pop = pd.read_csv('nycHistPop.csv',skiprows=5)


aresponse = input("Enter borough:")
print("Min:",pop[aresponse].min())
print("Min:",pop[aresponse].max())
print("Min:",pop[aresponse].mean())
print("Min:",pop[aresponse].median())
print("Min:",pop[aresponse].std())


