#Tommy Garica
#

def main():

    names = input("Please enter a list of names(separated by commas): ")

    person= names.split(";")
    for first in person:
        first=first.split(",")
        for last in first:
            print(last)
    





main()
