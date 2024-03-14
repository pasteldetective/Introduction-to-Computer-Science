#Name: Jackie Yee
#Date: 17 September 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 7

phrase = input("Enter Phrase Here Please")

for i in phrase:
    print(chr(ord(i)),ord(i)+1,chr(ord(i)+1))

