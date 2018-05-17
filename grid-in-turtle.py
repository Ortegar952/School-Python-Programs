#Tommy Garica
#Grid in turtle

import turtle
def main():
        
  
    alex=turtle.Turtle()
    alex.speed(0)

    for row in range(9):  #creates the rows
        for col in range(9):  #creates the columns
            alex.setpos(col * 50, row * 50)   
            alex.pendown()
            for square in range(4): #Loops through and draws the squares
                alex.forward(50)
                alex.left(90)
            alex.penup()
    alex.hideturtle()
    


main()
