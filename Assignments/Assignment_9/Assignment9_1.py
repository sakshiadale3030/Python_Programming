######################################################################
#
# User Defined Module
#
######################################################################

import Arithematic

######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          28/01/2026
######################################################################

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    print("Addition is : ",Arithematic.Addition(Value1,Value2))
    print("Substraction is : ",Arithematic.Substraction(Value1,Value2))
    print("Multiplication is : ",Arithematic.Multiplication(Value1,Value2))
    print("Division is : ",Arithematic.Division(Value1,Value2))

if __name__ == "__main__":
    main()