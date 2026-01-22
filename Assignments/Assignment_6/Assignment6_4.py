######################################################################
#  Function Name : Minimum()
#  Descripton :    Check the Minimum number
#  Parameter :     one number
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          21/01/2026
######################################################################

Minimum = lambda No1,No2 : No1 if No1 < No2 else No2     
  
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          21/01/2026
######################################################################

def main():
    Ret = 0

    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Ret = Minimum(Value1,Value2)   

    print("Minimum number is : ",Ret)

if __name__ == "__main__":
    main()    