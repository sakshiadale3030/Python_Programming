######################################################################
#  Function Name : Factorial()
#  Descripton :    Display the Factorial of given number
#  Parameter :     one number
#  Return :        Factorial of number
#  Author :        Sakshi Ashok Adale
#  Date :          17/01/2026
######################################################################

def Factorial(No):
    Fact = 1

    for i in range(1,No+1):
        Fact = Fact * i

    return Fact  

######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          17/01/2026
######################################################################

def main():
    Value = int(input("Enter number : "))

    Ret = Factorial(Value)  

    print("Factorial of number : ",Ret)  

if __name__ == "__main__":
    main()    