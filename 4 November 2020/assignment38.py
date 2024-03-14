#Name: Jackie Yee
#Date: 21 October 2020
#Email: jackie.yee14@myhunter.cuny.edu
#This program attempts to replicate the photo in assignment 38

import turtle
def setUp(t, dist, col):
    """
    Takes three parameters, a turtle, t, the distance, dist, 
    to move the turtle and a color, col, to set the turtle's color.
    """
    t.penup()
    t.forward(dist)
    t.pendown()
    t.color(col)


def squares(t, length):
    """
    Takes two parameters: a turtle and a length.
    The function does the following: if the length is greater than 10,
    it repeats 4 times:  moves forward that length, turns 90 degrees, 
    and calls squares(t, length/2).
    """
    x = 0
    if(length > 10):
        while x < 4:
            t.forward(length)
            t.right(90)
            x+=1
        squares(t, length/2)
    


     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ### Other than your name above, ###
     ### these are the only sections ###
     ### you change in this program. ###
     ###################################    


def nestedSquares(t, length):
    """
    Takes two parameters: a turtle and a length.
    The function does the following: if the length is greater than 10,
    it repeats 4 times:  moves forward that length, turns 90 degrees, 
    and calls nestedSquares(t, length/2).
    """

    x = 0
    if(length > 10):
        while x < 4:
            t.forward(length)
            t.right(90)
            x+=1
            nestedSquares(t, length/2)
            

     ###################################
     ### FILL IN YOUR CODE HERE      ###
     ### Other than your name above, ###
     ### these are the only sections ###
     ### you change in this program. ###
     ###################################       


def main():
    n = int(input('Enter length: '))

    tom = turtle.Turtle()
    setUp(tom, -100, "darkgreen")
    squares(tom, n)

    tess = turtle.Turtle()
    setUp(tess, 100, "steelblue")
    nestedSquares(tess, n)

if __name__ == "__main__":
     main()
