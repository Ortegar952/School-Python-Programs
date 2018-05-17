#Tommy Garcia
#Program asks the user for the name of a text file, and then prints to the
#screen each of the lines in the file in upper case letters.


def main():
    fname= input("Enter filename: ")
    infile= open(fname,"r")
    data= infile.read()
    print(data.upper())

main()
