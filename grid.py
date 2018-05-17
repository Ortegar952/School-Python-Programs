#Tommy Garcia
#Draws grid on turtle
import turtle

def main():
    alex=turtle.Turtle()
    win=turtle.Screen()
    alex.speed(0)
    alex.hideturtle()
    for i in range(20):
        alex.color("blue")
        alex.up()
        alex.goto(0,i*20)
        alex.down()
        alex.forward(305)

    alex.left(90)


    for i in range(20):
        alex.color("red")
        alex.up()
        alex.goto(i*16,0)
        alex.down()
        alex.forward(380)

main()
