#Name: Jackie Yee
#Date: 1 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 14

import turtle
hex_answer = input("Please enter your 6-digit hexadecimal number:")
alex = turtle.Turtle()
alex.shape("turtle")
alex.color('#' + hex_answer)
alex.stamp()
