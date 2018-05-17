#Tommy Garcia


def main():

    fname=input("Please enter filename: ")

    infile=open(fname,"r")

    data=infile.readlines()

    for words in data:
        print("The first letters of the lines in your file are:",words[0])













main()
