######################################################################
#  Function Name : ReverseDigit()
#  Descripton :    Reverse of Digits
#  Parameter :     one number
#  Return :        Sum
#  Author :        Sakshi Ashok Adale
#  Date :          18/01/2026
######################################################################

def ReverseDigit(No):
    Rev = 0
    Digit = 0

    while(No != 0):
        Digit = No % 10
        Rev = Rev*10 + Digit
        No = No // 10

    return Rev    

######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          18/01/2026
######################################################################

def main():
    Ret = 0

    Value = int(input("Enter number : "))

    Ret = ReverseDigit(Value)  

    print("Reverse of Digits : ",Ret)

if __name__ == "__main__":
    main()    