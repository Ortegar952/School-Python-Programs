#Tommy Garcia

def accomulator(list_string):

    s=[]

   

    for i in range(len(list_string)):
        
        s.append(len(list_string[i]))
    return s
        

def main():
    
    list_string=input("Enter list of strings: ").split(",")
    length_1= accomulator(list_string)
    
    
    print(length_1)

main()
