def main():

    fname=input("Please enter filename: ")

    infile=open(fname,"r")

    totalChar=0
    numWords=0

    for line in infile:
        words= line.split()

        for word in words:
            totalChar=totalChar+len(word)
            numWords=numWords+ 1
        


    print("The average word length is",totalChar/numWords)


main()


