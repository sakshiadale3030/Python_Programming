######################################################################
#  Function Name : Largest()
#  Descripton :    Find the largest number
#  Parameter :     one number
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          21/01/2026
######################################################################

Largest = lambda No1,No2,No3 : (No1 if (No1 > No2 and No1 > No3)else No2 if (No2 > No3) else No3)    
  
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
    Value3 = int(input("Enter the third number : "))

    Ret = Largest(Value1,Value2,Value3)

    print("Largest of Number : ",Ret)

if __name__ == "__main__":
    main()