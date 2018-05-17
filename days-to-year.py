#Tommy Garcia
#This program converts a number of days into years and days

def main():
    print("This program converts a number of days into years and days")
    print()

    days=eval(input("Enter number of days: "))
    years=days//365  # X days in years
    remainder=days%365  #Remainder indicates the amount of extra days 
    print() #Blank line
    print("This is equivalet to",years,"year(s) and",remainder,"days")

main()
