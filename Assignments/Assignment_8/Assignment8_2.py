######################################################################
#  Function Name : CheckEvenOdd()
#  Descripton :    It is used to check even or odd number
#  Parameter :     One Integer 
#  Return :        Boolean
#  Author :        Sakshi Ashok Adale
#  Date :          24/01/2026
######################################################################

def CheckEvenOdd(No):
    if(No % 2 == 0):
        return True
    else:
        return False
    
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          24/01/2026
######################################################################

def main():
    Ret = False

    Value = int(input("Enter number : "))

    Ret = CheckEvenOdd(Value)

    if(Ret == True):
        print("Even Number")
    else:
        print("Odd Number")    

if __name__ == "__main__":
    main()