#Tommy Garcia
#Finds the factorial of a whole number

def main():
    n = eval(input("Please enter a whole number: "))
    fact = 1
    for factor in range(n,2,-1): 
       fact = fact * factor
    print("The factorial of", n, "is", fact)

main()
