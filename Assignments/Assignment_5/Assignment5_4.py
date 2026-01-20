import math

######################################################################
#  Function Name : Binary()
#  Descripton :    convert number into binary
#  Parameter :     one number
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          19/01/2026
######################################################################

def Binary(No):
    print("Binary : ",bin(No)[2:])
  
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          19/01/2026
######################################################################

def main():
    Value = int(input("Enter number : "))

    Binary(Value)   

if __name__ == "__main__":
    main()    