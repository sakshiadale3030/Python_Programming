#############################################################################
#  Function Name : Power()
#  Descripton :    It is used to calculate power of 2 for the given number
#  Parameter :     Integer 
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          02/02/2026
#############################################################################

Power = lambda No : 2**No
        
#############################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          02/02/2026
#############################################################################

def main():
    Ret = 0

    Value = int(input("Enter the number : "))

    Ret = Power(Value)

    print("Power of 2 : ",Ret)

if __name__ == "__main__":
    main()