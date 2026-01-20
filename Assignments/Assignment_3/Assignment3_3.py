######################################################################
#  Function Name : SumDigit()
#  Descripton :    Sum of Digits
#  Parameter :     one number
#  Return :        Sum
#  Author :        Sakshi Ashok Adale
#  Date :          18/01/2026
######################################################################

def SumDigit(No):
    Sum = 0
    Digit = 0

    while(No != 0):
        Digit = No % 10
        Sum = Sum + Digit
        No = No // 10

    return Sum     

######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          18/01/2026
######################################################################

def main():
    Ret = 0

    Value = int(input("Enter number : "))

    Ret = SumDigit(Value)  

    print("Sum of Digits : ",Ret)

if __name__ == "__main__":
    main()    