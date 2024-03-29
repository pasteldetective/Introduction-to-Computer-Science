#Name: Jackie Yee
#Date: 6 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 22
                
#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np

presponse = input("Enter file name:")
ca = plt.imread(presponse)   #Read in image
countSnow = 0            #Number of pixels that are almost white
t = 0.8                 #Threshold for almost white-- can adjust between 0.0 and 1.0

#For every pixel:
for i in range(ca.shape[0]):
     for j in range(ca.shape[1]):
          #Check if red, green, and blue are > t:
          if (ca[i,j,0] > t) and (ca[i,j,1] > t) and (ca[i,j,2] > t):
               countSnow = countSnow + 1

print("Snow count is", countSnow)        
