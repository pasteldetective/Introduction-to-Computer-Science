#Name: Jackie Yee
#Date: 6 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 15

#Import the packages for images and arrays:
import matplotlib.pyplot as plt
import numpy as np


answerimg = input('Enter name of the input file:')

img = plt.imread(answerimg + '.png')   #Read in image from csBridge.png

img2 = img.copy()        #make a copy of our image
img2[:,:,0] = 1
img2[:,:,2] = 1


plt.imsave('nogreenH.png', img2)  #Save the image we created to the file: reds.png
