######################################################################
#  Function Name : Display()
#  Descripton :    Check the number is positive or negative or zero
#  Parameter :     one integer 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          24/01/2026
######################################################################

def Display(No):
    if(No > 0):
        print("Number is Positive")
    elif(No == 0):
        print("Number is Zero")
    else:
        print("Number is negative")        
    
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          24/01/2026
######################################################################

def main():
    Value = int(input("Enter number : "))

    Display(Value) 

if __name__ == "__main__":
    main()