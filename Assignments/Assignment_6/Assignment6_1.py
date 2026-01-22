######################################################################
#  Function Name : Square()
#  Descripton :    Calculate the square of number
#  Parameter :     one number
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          21/01/2026
######################################################################

Square = lambda No : (No**2)       
  
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          21/01/2026
######################################################################

def main():
    Ret = 0

    Value = int(input("Enter number : "))

    Ret = Square(Value)   

    print("Square of number : ",Ret)

if __name__ == "__main__":
    main()    