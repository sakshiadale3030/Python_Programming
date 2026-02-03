#############################################################################
#
# User Defined Module
#
#############################################################################

import MarvellousNum

#############################################################################
#  Function Name : ListPrime()
#  Descripton :    It is used to do addition of all prime number from list is
#  Parameter :     Integer 
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          02/02/2026
#############################################################################

def ListPrime(Arr):
    Sum = 0

    for No in Arr:
        if MarvellousNum.ChkPrime(No):
            Sum = Sum + No
    return Sum
        
#############################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          02/02/2026
#############################################################################

def main():
    Ret = 0

    Size = int(input("Enter the No of elements : "))
    Data = []
    for i in range(Size):
        Data.append(int(input(f"Enter elements {i+1}: ")))
    print("Actual Data is : ",Data)    

    Ret = ListPrime(Data)

    print("Addition of all prime number from list is : ",Ret)

if __name__ == "__main__":
    main()