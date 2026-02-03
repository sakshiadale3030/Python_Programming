######################################################################
#  Function Name : isPrime()
#  Descripton :    Check the number is prime or not
#  Parameter :     Integer 
#  Return :        Boolean
#  Author :        Sakshi Ashok Adale
#  Date :          28/01/2026
######################################################################

def isPrime(No):
    if No <= 1:
        return False
    for i in range(2,No):
        if(No % i == 0):
            return False
    return True    

######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          28/01/2026
######################################################################

def main():
    Ret = False

    Value = int(input("Enter the number : "))

    Ret = isPrime(Value)

    if(Ret == True):
        print("It is prime number")
    else:
        print("It is not prime number")    
    
if __name__ == "__main__":
    main()