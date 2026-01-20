import math

######################################################################
#  Function Name : Perfect()
#  Descripton :    Check the perfect number
#  Parameter :     one number
#  Return :        boolean
#  Author :        Sakshi Ashok Adale
#  Date :          19/01/2026
######################################################################

def Grade(marks):
    if(marks >= 75):
        print("Distinction")
    elif(marks >= 60):
        print("First Class")
    elif(marks >= 50):
        print("Second Class")
    else:
        print("Fail")            
  
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          19/01/2026
######################################################################

def main():
    Value = int(input("Enter number : "))

    Grade(Value)   

if __name__ == "__main__":
    main()    