#############################################################################
#  Function Name : Multiplication()
#  Descripton :    It is used to calculate multiplication of two number
#  Parameter :     Integer 
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          02/02/2026
#############################################################################

Multiplication = lambda No1, No2 : No1 * No2
        
#############################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          02/02/2026
#############################################################################

def main():
    Ret = 0

    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Ret = Multiplication(Value1,Value2)

    print("Multiplication of two number : ",Ret)

if __name__ == "__main__":
    main()