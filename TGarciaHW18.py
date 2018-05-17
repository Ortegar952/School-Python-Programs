#Tommy Garcia
#


def main():

    fname=input("Please enter filename: ")
    infile=open(fname,"r")
    data=infile.readlines()
    for words in data:
       print ("Line character count is",len(words.strip('\n')))
        





main()

