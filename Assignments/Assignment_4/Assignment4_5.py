######################################################################
#  Function Name : DisplayReverse()
#  Descripton :    Display the reverse number
#  Parameter :     one number
#  Return :        Noting
#  Author :        Sakshi Ashok Adale
#  Date :          19/01/2026
######################################################################

def DisplayReverse(No):
   for i in range(1,No+1):
       print(i,end=" ")
    
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          19/01/2026
######################################################################

def main():
    Value= int(input("Enter number : "))

    DisplayReverse(Value)  

if __name__ == "__main__":
    main()    