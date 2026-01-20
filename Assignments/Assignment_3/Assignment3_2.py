######################################################################
#  Function Name : CountDigit()
#  Descripton :    Count Digits in number
#  Parameter :     one number
#  Return :        Count
#  Author :        Sakshi Ashok Adale
#  Date :          18/01/2026
######################################################################

def CountDigit(No):
    iCount = 0

    while(No != 0):
        iCount += 1
        No = No // 10

    return iCount     

######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          18/01/2026
######################################################################

def main():
    Ret = 0

    Value = int(input("Enter number : "))

    Ret = CountDigit(Value)  

    print("Count of Digits : ",Ret)

if __name__ == "__main__":
    main()    