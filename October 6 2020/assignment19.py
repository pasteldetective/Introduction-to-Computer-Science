#Name: Jackie Yee
#Date: 6 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 19

presponse = int(input('Enter the number of cents:'))
print("Quarters:", int(presponse/25))
estRem = presponse % 25
print("Dimes:", int(estRem / 10))
estRem = estRem % 10
print("Nickels:", int(estRem / 5))
print("Cents:", int(presponse % 5))