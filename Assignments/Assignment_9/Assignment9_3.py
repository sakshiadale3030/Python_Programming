######################################################################
#  Function Name : Factorial()
#  Descripton :    It is used to find Factorial of number
#  Parameter :     Integer 
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          28/01/2026
######################################################################

def Factorial(No):
    Fact = 1

    for i in range(1,No+1):
        Fact = Fact*i
    return Fact      

######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          28/01/2026
######################################################################

def main():
    Ret = 0

    Value = int(input("Enter the number : "))

    Ret = Factorial(Value)

    print("Factorial is : ",Ret)
    
if __name__ == "__main__":
    main()