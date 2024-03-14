#Name: Jackie Yee
#Date: 6 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 16

presponse = int(input('Please enter the time in seconds:'))
calhours = (int(presponse/3600))
calmins = (int((presponse - calhours*3600)/60))
calsecs = (int(presponse % 60))
strhours = str(calhours) + "h:"
strmins = str(calmins) + "m:"
strsecs = str(calsecs) + "s"
print(strhours,strmins,strsecs)

