#Name: Jackie Yee
#Date: 17 September 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 9

phrase = input()
phrase = (phrase.upper())
print("Your phrase in capital letters:", phrase)
phrase_split = phrase.split()
concat = ""
for i in phrase_split:
    concat += (i[:1])

print("ACHRONYM:", concat)
