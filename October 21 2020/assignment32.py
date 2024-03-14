#Name: Jackie Yee
#Date: 21 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 34
                

import pandas as pd
import matplotlib.pyplot as plt

Iresponse = input("Enter name of input file:")
Oresponse = input("Enter name of output file:")

homeless = pd.read_csv(Iresponse)
homeless['Date'] = homeless.to_datetime(homeless['Date'].apply(str))
homelessPre = homeless.groupby('Present')

plt.gcf().subplots_adjust(bottom=0.5)
fig = plt.gcf()
fig.savefig(Oresponse)
