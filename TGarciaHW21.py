#Tommy Garcia


def main():

    fname = input("Please enter your file name: ")

    RunningSum = 0

    openfile = open(fname, "r")

    for line in openfile:
         for num in line.split(','):
              RunningSum = RunningSum + float(num.strip())


    print("The sum of your numbers is %.1f" %(RunningSum))

    

        
        

        
        



main()        
    
