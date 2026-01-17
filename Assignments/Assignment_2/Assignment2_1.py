######################################################################
#  Function Name : MultTable()
#  Descripton :    Display the Multiplication Table
#  Parameter :     one number
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          17/01/2026
######################################################################

def MultTable(No):
    for i in range(1,10+1):
        print("",(No*i))

######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          17/01/2026
######################################################################

def main():
    Value = int(input("Enter number : "))

    Ret = MultTable(Value)    

if __name__ == "__main__":
    main()    