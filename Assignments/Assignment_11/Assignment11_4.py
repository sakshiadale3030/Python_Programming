from functools import reduce

#############################################################################
#  Function Name : CheckEven()
#  Descripton :    It is used to check the even number
#  Parameter :     Integer 
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          02/02/2026
#############################################################################

CheckEven = lambda No : No % 2 == 0

#############################################################################
#  Function Name : Square()
#  Descripton :    It is used to square the numbers from list
#  Parameter :     Integer 
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          02/02/2026
#############################################################################

Square = lambda No : No**2

#############################################################################
#  Function Name : Addition()
#  Descripton :    It is used to do addition of all numbers
#  Parameter :     Integer 
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          02/02/2026
#############################################################################

Addition = lambda No1,No2 : No1+No2
        
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

    FData = list(filter(CheckEven,Data))
    print("Data after filter is : ",FData)

    MData = list(map(Square,FData))
    print("Data after map is : ",MData)

    RData = reduce(Addition,MData)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()