#Name: Jackie Yee
#Date: 6 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 21
                
import matplotlib.pyplot as plt
import numpy as np

presponse = int(input('Enter the size:'))
pquestion = input('Enter output file:')

imger = np.zeros((presponse,presponse,3))

for x in range(presponse):
    if (x % 2 == 0):
        imger[x:x+1,:,1] = 1.0
    else:
        imger[x:x+1,:,0] = 1.0
        imger[x:x+1,:,1] = 1.0
        imger[x:x+1,:,2] = 1.0


#Save the image:
plt.imsave(pquestion, imger)
    
        
