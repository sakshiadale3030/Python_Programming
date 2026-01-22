######################################################################
#  Function Name : Divide()
#  Descripton :    Check the Divisible by 5
#  Parameter :     one number
#  Return :        Boolean
#  Author :        Sakshi Ashok Adale
#  Date :          21/01/2026
######################################################################

Divide = lambda No : (No % 5 == 0)      
  
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          21/01/2026
######################################################################

def main():
    Ret = 0

    Value = int(input("Enter the number : "))

    Ret = Divide(Value)

    print("Divisible by 5 : ",Ret)

if __name__ == "__main__":
    main()