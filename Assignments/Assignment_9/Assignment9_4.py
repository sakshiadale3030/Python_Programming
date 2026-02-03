######################################################################
#  Function Name : Factors()
#  Descripton :    It is used to do sum of Factors
#  Parameter :     Integer 
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          28/01/2026
######################################################################

def Factors(No):
    Sum = 0

    for i in range(1,No):
        if(No % i == 0):
            Sum = Sum + i
    return Sum     

######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          28/01/2026
######################################################################

def main():
    Ret = 0

    Value = int(input("Enter the number : "))

    Ret = Factors(Value)

    print("Sum of Factors : ",Ret)
    
if __name__ == "__main__":
    main()