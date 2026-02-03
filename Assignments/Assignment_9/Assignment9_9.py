######################################################################
#  Function Name : CountDigit()
#  Descripton :    It is used to Count the Digit
#  Parameter :     Integer 
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          28/01/2026
######################################################################

def CountDigit(No):
    iCount = 0

    while No > 0:
        iCount = iCount + 1  
        No = No // 10
    return iCount    

######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          28/01/2026
######################################################################

def main():
    Ret = 0

    Value = int(input("Enter the number : "))

    Ret = CountDigit(Value)

    print("Count of digits are : ",Ret)

if __name__ == "__main__":
    main()