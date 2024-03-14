#Name: Jackie Yee
#Date: 21 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 31
                

import pandas as pd
import matplotlib.pyplot as plt

aresponse = input("Enter name of input file:")
bresponse = input("Enter name of output file:")



homeless = pd.read_csv(aresponse)
homeless['Fraction Single Women'] = homeless['Single Adult Women in Shelter']/homeless['Total Individuals in Shelter']
homeless.plot(x = "Date of Census", y = "Fraction Single Women")

fig = plt.gcf()
fig.savefig(bresponse)
