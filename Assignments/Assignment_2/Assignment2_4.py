######################################################################
#  Function Name : DisplayEven()
#  Descripton :    Display the Even number till that number
#  Parameter :     one number
#  Return :        nothing
#  Author :        Sakshi Ashok Adale
#  Date :          17/01/2026
######################################################################

def DisplayEven(No):
    for i in range(1,No+1):
        if(i % 2 == 0):
            print("",i) 

######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          17/01/2026
######################################################################

def main():
    Value = int(input("Enter number : "))

    DisplayEven(Value)  

if __name__ == "__main__":
    main()    