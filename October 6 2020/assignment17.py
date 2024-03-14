#Name: Jackie Yee
#Date: 6 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 17

import turtle
presponse = int(input('Enter number of stamps the turtle will print:'))
alex = turtle.Turtle()
alex.shape("circle")
alex.penup()
step = 20
for x in range(presponse):
    alex.stamp()
    if (x%4 == 0):
        step += 2
    alex.forward(step)
    alex.right(24)
    
        
