#Tommy Garcia



def getNum():

    return int(input("Enter a number between 0 and 1000, inclusive: "))

def condition():

    i = getNum()

    while i < 0 or i > 1000:

        print("Number is out of range. Please try again!")
        print()

        i = getNum()

    return i



def main():

    q = condition()

    print(q)


main()
