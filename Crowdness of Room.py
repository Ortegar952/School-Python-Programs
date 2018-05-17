#Tommy Garcia
#Determines if room is crowded based on the number of names entered
def reviewlist(list_names):

    x=len(list_names)

    if x==0:
        print("Room is empty")

    elif x==1 or x==2:
        print("Room isn't crowded")
    elif x==3 or x==4 or x==5:
        print ("Room is crowded")
    elif x>5:
        print("There's a mob in the room")


def main():

    names=input("Enter name: ")

    list_names=[]

    while names != "":

        names=input("Enter name: ")

        list_names.append(names)
        
    y = reviewlist(list_names)

main()
    
