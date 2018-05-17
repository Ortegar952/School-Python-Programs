#Tommy Garcia

import turtle


#doAction() takes a turtle and a character and has the turtle perform
#   action indicated by the character
def doAction(t,c):
    if c == 'F':            #move forward
        t.forward(50)
    elif c == 'L':          #turn left
        t.left(90)
    elif c == 'R':          #turn right
        t.right(90)
    elif c == '^':          #lift pen
        t.up()
    elif c == 'v':          #lower pen
        t.down()
    elif c == "B":          #moves backwards
        t.backward(50)
    elif c == "r":          #change color to red
        t.color("red")
    elif c == "g":          #change color to green
        t.color("green")
    elif c == "b":          #change color to blue
        t.color("blue")


    
    else:                   #for any other character, print an error message 
        print("Error: do not know the command:", c)


def main():
    silas = turtle.Turtle()
    myWin = turtle.Screen()     #The graphics window
    commands = input("Please enter a command string: ")
    for ch in commands:
        doAction(silas,ch)

    print("See graphics window for your image")
    myWin.exitonclick()         #Close the window when clicked

main()
