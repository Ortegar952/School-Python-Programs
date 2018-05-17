#Tommy Garcia
#This program computes the area of a room.


def main():
    name= input("Type your name: ")
    length=eval(input("Enter length in feets: "))
    width=eval(input("Enter width in feets: "))
    area=(length*width)

    print(name,",the area is", area,"square ft")
    print("\t In sq yards, it is", area/9)
    
        

main()
