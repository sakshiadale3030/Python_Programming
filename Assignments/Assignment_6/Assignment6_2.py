######################################################################
#  Function Name : Cube()
#  Descripton :    Calculate the cube of number
#  Parameter :     one number
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          21/01/2026
######################################################################

Cube = lambda No : (No**3)       
  
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          21/01/2026
######################################################################

def main():
    Ret = 0

    Value = int(input("Enter number : "))

    Ret = Cube(Value)   

    print("Cube of number : ",Ret)

if __name__ == "__main__":
    main()    