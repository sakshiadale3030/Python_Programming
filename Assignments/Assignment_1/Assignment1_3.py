######################################################################
#  Function Name : square()
#  Descripton :    Display the square of number
#  Parameter :     one numbers
#  Return :        square of number
#  Author :        Sakshi Ashok Adale
#  Date :          17/01/2026
######################################################################

def square(No):
    Squ = No**2

    return Squ

######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          17/01/2026
######################################################################

def main():
    Value = int(input("Enter number : "))

    Ret = square(Value)

    print("Square of given number is : ",Ret)

if __name__ == "__main__":
    main()    