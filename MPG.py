#Tommy Garcia
#Determines the Miles Per Gallon
def main():

    start_m=eval(input("Enter starting mileage: "))
    inStr=input("Enter amount of miles and gallons (separeted by commas): ")

    MPGlist=[]
    while inStr !="":
        endMiles,gallons=eval(inStr)
        MPG=(endMiles-start_m)/gallons
        MPGlist.append(MPG)

        startMiles=endMiles
        inStr=input("Enter amount of miles and gallons (separeted by commas): ")

    for i in range(len(MPGlist)):
        print("Leg"+str(i+1), "MPG",MPGlist[i])


main()
        
        










