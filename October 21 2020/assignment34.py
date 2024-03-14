#Name: Jackie Yee
#Date:1 November 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 34
                

import pandas as pd
import matplotlib.pyplot as plt

Iresponse = input("Enter name of input file:")
Oresponse = input("Enter name of output file:")

student = pd.read_csv(Iresponse)
student["Date"] = pd.to_datetime(student["Date"].apply(str))
student["% Attending"] = student["Present"]/student["Enrolled"]*100
student.plot(x = "Date", y = "% Attending")
plt.show()

fig = plt.gcf()
fig.savefig(Oresponse)
