#Tommy Garcia
#Program that prompts the user to enter 5 lines
#of text and then outputs the total number of characters that they entered.


def main():




    RunningLine=""

    for i in range(5):
        line=input("Enter line: ")
        print("Line character count is",len(line))
        RunningLine=RunningLine+line




    print("The number of characters entered is:",(len(RunningLine)))












main()
