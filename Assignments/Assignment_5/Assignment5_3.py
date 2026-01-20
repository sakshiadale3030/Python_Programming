import math

######################################################################
#  Function Name : Perfect()
#  Descripton :    Check the perfect number
#  Parameter :     one number
#  Return :        boolean
#  Author :        Sakshi Ashok Adale
#  Date :          19/01/2026
######################################################################

def Perfect(No):
    Sum = 0

    for i in range(1,No):
       if(No % i == 0):
           Sum = Sum + i
    if(Sum == No):
        return True
    else:
        return False  

    
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          19/01/2026
######################################################################

def main():
    Ret = 0

    Value = int(input("Enter number : "))

    Ret = Perfect(Value)  

    if(Ret == True):
        print("Number is perfect")
    else:
         print("Number is not perfect")   

if __name__ == "__main__":
    main()    