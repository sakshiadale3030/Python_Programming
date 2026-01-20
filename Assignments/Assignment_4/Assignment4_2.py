######################################################################
#  Function Name : Factor()
#  Descripton :    find factor of number
#  Parameter :     Number
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          19/01/2026
######################################################################

def Factor(No):
    for i in range(1,No+1):
        if(No % i == 0):
            print(i)
       
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          19/01/2026
######################################################################

def main():
    Value = int(input("Enter number : "))

    Factor(Value)  

if __name__ == "__main__":
    main()    