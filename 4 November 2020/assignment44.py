#Name: Jackie Yee
#Date: 21 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 44

#CSci 127 Teaching Staff
#October 2020
#A program that draws concentric colored circles, but filled with errors...

#Modified by: ADD YOUR NAME AND EMAIL HERE

import turtle
import random


print("\nThis program draws concentric circles of many different colors\n")
# prompt for the input
fig_num = int(input("Enter the number of circles to draw: "))
radius = int(input("/nEnter the radius (>=50, <=200) of the largest circle:\n "))

#set the decrement for each concentric radius
decrement = radius/fig_num

#initialize turtle
tina = turtle.Turtle()

# draw fig_num filled concentric circles, randomly changing colors
for j in range(fig_num):
    #move the turtle to the -radius y coordinate
    tina.up()
    tina.goto(0,-radius)

    #set a random color
    (r,g,b) = (random.random(), random.random(), random.random())
    tina.pencolor(r,g,b)
    tina.fillcolor(r,g,b)

    #draw the circle
    tina.down()
    tina.begin_fill()
    tina.circle(radius)
    tina.end_fill()

    #decrement the radius for the next concentri circle
    radius -= decrement

turtle.Screen().exitonclick()
