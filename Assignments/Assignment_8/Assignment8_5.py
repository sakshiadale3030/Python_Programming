######################################################################
#  Function Name : Display()
#  Descripton :    It is used to Display the string
#  Parameter :     one integer 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          24/01/2026
######################################################################

def Display(No):
    for i in range(No,0,-1):
        print(i)
    
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