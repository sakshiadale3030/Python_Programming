######################################################################
#  Function Name : Add()
#  Descripton :    It is used for addition of two number
#  Parameter :     Nothing 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          24/01/2026
######################################################################

def Add(No1,No2):
    Ans = 0

    Ans = No1 + No2

    return Ans
    
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          24/01/2026
######################################################################

def main():
    Ret = 0

    Value1 = int(input("Enter first number : "))
    Value2 = int(input("Enter second number : "))

    Ret = Add(Value1,Value2)

    print("Addition is : ",Ret)  

if __name__ == "__main__":
    main()