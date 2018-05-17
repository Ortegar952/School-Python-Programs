#Tommy Garcia
#This program converts a number of days into years and days

def main():
    print("This program converts a number of days into years and days")
    print()

    days=eval(input("Enter number of days: "))
    years=days//365
    months=days%365
    months_2=months//30
    weeks=months_2//4
    days_2=weeks//7

    print()
    print("This is equivalent to",years,"years,",months_2,"months,",weeks,"weeks, and",days_2,"days")
    
    




main()
    
    
