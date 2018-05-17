def numbers(num_list):

    square=[]

    for i in num_list:
        square.append(i**2)

    return square
        
    


        
def main():
    num_list=[3,-1,0,2,10]
    
    print(num_list,"Squared is equal to",numbers(num_list))

main()

