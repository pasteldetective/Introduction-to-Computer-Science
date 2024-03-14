#Name: Jackie Yee
#Date: 14 September 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 5

import turtle
wn = turtle.Screen()
wn.bgcolor("hotpink")

alex = turtle.Turtle()
alex.pencolor("red")
alex.fillcolor("yellow")
alex.shape("turtle")


for i in range(36):
    alex.forward(200)
    alex.right(170)
    alex.stamp()



wn.exitonclick()
