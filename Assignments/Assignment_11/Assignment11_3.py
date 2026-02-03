from functools import reduce

#############################################################################
#  Function Name : Greater()
#  Descripton :    It is used to find the number greater than 70 and less 
#                  less than 90
#  Parameter :     Integer 
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          02/02/2026
#############################################################################

Greater = lambda No : No >= 70 and No <= 90

#############################################################################
#  Function Name : Increment()
#  Descripton :    It is used to increment the numbers from the list by 10
#  Parameter :     Integer 
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          02/02/2026
#############################################################################

Increment = lambda No : No + 10

#############################################################################
#  Function Name : Product()
#  Descripton :    It is used to do product of all numbers from list
#  Parameter :     Integer 
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          02/02/2026
#############################################################################

Product = lambda No1,No2 : No1*No2
        
#############################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          02/02/2026
#############################################################################

def main():
    Ret = 0

    Size = int(input("Enter the number of elements : "))
    Data = []

    for i in range(Size):
        Data.append(int(input(f"Ente the element {i+1} : ")))
    print("Actual Data is : ",Data)

    FData = list(filter(Greater,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Increment,FData))
    print("Data after map is : ",MData)

    RData = reduce(Product,MData)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()