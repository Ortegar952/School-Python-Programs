#Tommy Garcia
#Prints a user specified sentence a user specified number of times

def main():
    sentence=input("Enter your sentence: ")
    ntimes=eval(input("Enter number of times to print it: "))

    for i in range(ntimes):
        print(i+1,sentence)

main()
