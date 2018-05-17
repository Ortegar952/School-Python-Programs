#Tommy Garcia
#Program asks the user for the name of a text file, and then prints to the screen the first character in each line.

def main():

    RunningSum=0

    

    fname=input("Enter file name: ")

    infile=open(fname,"r")


    for nums in infile:
        RunningSum=RunningSum + float(nums)
    print("The sum of your numbers is", RunningSum)








main()

