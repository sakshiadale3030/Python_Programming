######################################################################
#  Function Name : Odd()
#  Descripton :    Check the Odd number
#  Parameter :     one number
#  Return :        Boolean
#  Author :        Sakshi Ashok Adale
#  Date :          21/01/2026
######################################################################

Odd = lambda No : (No % 2 != 0)      
  
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          21/01/2026
######################################################################

def main():
    Ret = 0

    Value = int(input("Enter the number : "))

    Ret = Odd(Value)

    print("Number is Odd : ",Ret)

if __name__ == "__main__":
    main()