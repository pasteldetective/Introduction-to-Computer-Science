#Name: Jackie Yee
#Date: 1 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 12

import turtle

turtle.colormode(255)
alex = turtle.Turtle()
alex.shape("turtle")
alex.backward(100)

for i in range(0,255,10):
    alex.forward(20)
    alex.pensize(i)
    alex.color(255 - i ,0,i)

