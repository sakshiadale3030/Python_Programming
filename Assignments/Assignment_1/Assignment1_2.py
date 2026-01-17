######################################################################
#  Function Name : checkGreater()
#  Descripton :    Check which number is greater
#  Parameter :     Two numbers
#  Return :        Greater number
#  Author :        Sakshi Ashok Adale
#  Date :          17/01/2026
######################################################################

def checkGreater(No1,No2):
    if(No1 > No2):
        return No1
    else:
        return No2

######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          17/01/2026
######################################################################

def main():
    Value1 = int(input("Enter the first number : "))
    Value2 = int(input("Enter the second number : "))

    Ret = checkGreater(Value1,Value2)

    print("Greater number is : ",Ret)

if __name__ == "__main__":
    main()    