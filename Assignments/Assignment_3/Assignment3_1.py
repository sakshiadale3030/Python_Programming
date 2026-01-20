######################################################################
#  Function Name : CheckPrime()
#  Descripton :    Check number is prime or not
#  Parameter :     one number
#  Return :        boolean
#  Author :        Sakshi Ashok Adale
#  Date :          18/01/2026
######################################################################

def CheckPrime(No):
    if(No % 2 == 0):
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

    Ret = CheckPrime(Value)  

    if(Ret == True):
        print("Number is prime")
    else:
         print("Number is not prime")    

if __name__ == "__main__":
    main()    