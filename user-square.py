#Tommy Garcia
#Program draws a square using user specified color
#and a user specified length for the side of the square.

import turtle
def main():

    alex=turtle.Turtle()
    alex.color(input("Enter desired color: "))
    length=eval(input("Enter length: "))
    for x in range(4):
        alex.forward(length)
        alex.left(90)
    alex.hideturtle()





main()
