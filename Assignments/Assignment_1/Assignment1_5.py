######################################################################
#  Function Name : CheckDivisible()
#  Descripton :    Check 3 and 5 are divisible by 3 and 5
#  Parameter :     one numbers
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          17/01/2026
######################################################################

def CheckDivisible(No):
    if((No % 3 == 0) & (No % 5 == 0)):
        return True
    else:
        return False

######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          17/01/2026
######################################################################

def main():
    Value = int(input("Enter number : "))

    Ret = CheckDivisible(Value)

    if(Ret == True):
        print("Divisible by 3 and 5")
    else:
        print("Not Divisible by 3 and 5")    

if __name__ == "__main__":
    main()    