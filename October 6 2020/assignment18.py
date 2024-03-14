#Name: Jackie Yee
#Date: 6 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 18

import matplotlib.pyplot as plt
import numpy as np
imger = np.zeros((30,30,3))

imger[0:20,10:20,0] = 1.0
imger[0:20,10:20,1] = 1.0
imger[0:20,10:20,2] = 1.0

imger[:,0:10,2] = 1.0
imger[20:30,10:20,2] = 1.0
imger[:,20:30,2] = 1.0


plt.imsave("logo.png",imger)
    
        
