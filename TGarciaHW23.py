#Tommy Garcia

def main():

    fname=input("Enter filename: ")

    openfile=open(fname,"r")


    lenght=eval(input("Enter desired lenght of line: "))
    print()



    for lines in openfile:        
        print(lines[:lenght])
        print(lines[lenght:])
        



    
    










main()
