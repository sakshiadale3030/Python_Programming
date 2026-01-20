######################################################################
#  Function Name : Addition()
#  Descripton :    Addition of two number 
#  Parameter :     two number
#  Return :        Addition
#  Author :        Sakshi Ashok Adale
#  Date :          19/01/2026
######################################################################

def Addition(No1,No2):
    Ans = 0

    Ans = No1 + No2

    return Ans

######################################################################
#  Function Name : Subtraction()
#  Descripton :    Substraction of two number
#  Parameter :     two number
#  Return :        Subtraction
#  Author :        Sakshi Ashok Adale
#  Date :          19/01/2026
######################################################################

def Subtraction(No1,No2):
    Ans = 0

    Ans = No1 - No2

    return Ans

######################################################################
#  Function Name : Multiplication()
#  Descripton :    Multiplication of two number
#  Parameter :     two number
#  Return :        Multiplication
#  Author :        Sakshi Ashok Adale
#  Date :          19/01/2026
######################################################################

def Multiplication(No1,No2):
    Ans = 0

    Ans = No1 * No2

    return Ans

######################################################################
#  Function Name : Division()
#  Descripton :    Division of two number
#  Parameter :     two number
#  Return :        Division
#  Author :        Sakshi Ashok Adale
#  Date :          19/01/2026
######################################################################

def Division(No1,No2):
    Ans = 0

    Ans = No1 / No2

    return Ans
    
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          19/01/2026
######################################################################

def main():
    Ret = False

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Addition(Value1,Value2)  
    print("Addition is : ",Ret)

    Ret = Subtraction(Value1,Value2)  
    print("Subtraction is : ",Ret)

    Ret = Multiplication(Value1,Value2)  
    print("Multiplication is : ",Ret)

    Ret = Division(Value1,Value2)  
    print("Division is : ",Ret)

if __name__ == "__main__":
    main()    