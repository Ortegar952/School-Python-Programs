#Tommy Garcia

def main():

    a,b,c,d,f=eval(input("Enter the prices: "))
    
    numbers=a,b,c,d,f

    print("Your receipt:")

    for digits in numbers:
        print("${0:6.2f}".format(digits))
        
    
    total=a+b+c+d+f
    

    print("--------\n"     "Total:${:.2f}".format(a+b+c+d+f))


    


















main()
