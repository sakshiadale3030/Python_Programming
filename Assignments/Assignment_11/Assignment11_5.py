from functools import reduce

#############################################################################
#  Function Name : is_prime()
#  Descripton :    It is used to check the prime number
#  Parameter :     Integer 
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          02/02/2026
#############################################################################

def is_prime(No):
    if No <= 1:
        return False
    for i in range(2,int(No**0.5)+1):
        if(No % i == 0):
            return False
    return True    

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

    FData = list(filter(is_prime,Data))
    print("Data after filter is : ",FData)

    MData = list(map(lambda No : No * 2,FData))
    print("Data after map is : ",MData)

    RData = reduce(lambda No1,No2 : No1 if No1 > No2 else No2,MData)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()