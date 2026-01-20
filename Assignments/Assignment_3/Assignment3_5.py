######################################################################
#  Function Name : Palindrome()
#  Descripton :    Number is Palindrome or not
#  Parameter :     one number
#  Return :        Sum
#  Author :        Sakshi Ashok Adale
#  Date :          18/01/2026
######################################################################

def Palindrome(No):
    Original = No
    Rev = 0
    Digit = 0

    while(No != 0):
        Digit = No % 10
        Rev = Rev*10 + Digit
        No = No // 10

    if(Original == Rev):
        return True
    else:
        return False
       

######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          18/01/2026
######################################################################

def main():
    Ret = False

    Value = int(input("Enter number : "))

    Ret = Palindrome(Value)  

    if(Ret == True):
        print("Number is Palindrome")
    else:
        print("Number is not Palindrome")

if __name__ == "__main__":
    main()    