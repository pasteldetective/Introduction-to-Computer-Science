#Name: Jackie Yee
#Date: 1 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 13

name = input("Please enter your list of names:")
name_split = name.split('; ')

for i in name_split:
    name_list = i.split(', ')
    print(name_list[1][0] + ".", name_list[0])



