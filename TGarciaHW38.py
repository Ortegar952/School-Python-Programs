#Tommy Garcia

def main():

    infile = open("infile.txt","r")

    data = infile.read()

    MyList = []
    
    for lines in data.split("\n"):
        MyList.append(lines)

    MyWords = []

    for words in MyList:
        if len(words) > 5:
            print(words)
        else:
            break

        
    
    


        

        
    









main()

