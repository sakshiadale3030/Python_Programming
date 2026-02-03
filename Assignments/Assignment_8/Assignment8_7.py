######################################################################
#  Function Name : Divisible()
#  Descripton :    Check the number is divisible by 5 or not
#  Parameter :     one integer 
#  Return :        Boolean
#  Author :        Sakshi Ashok Adale
#  Date :          28/01/2026
######################################################################

def Divisible(No):
    if(No % 5 == 0):
        return True
    else:
        return False       
    
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          28/01/2026
######################################################################

def main():
    Ret = False

    Value = int(input("Enter number : "))

    Ret = Divisible(Value) 

    if(Ret == True):
        print("Divisible by 5")
    else:
        print("Not Divisible by 5")    

if __name__ == "__main__":
    main()