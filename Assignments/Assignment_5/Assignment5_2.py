import math

######################################################################
#  Function Name : Circle()
#  Descripton :    Calculate the area of circle
#  Parameter :     one number
#  Return :        Area
#  Author :        Sakshi Ashok Adale
#  Date :          19/01/2026
######################################################################

def Circle(Radius):
   Area = 0

   Area = math.pi * (Radius**2)

   return Area
    
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          19/01/2026
######################################################################

def main():
    Ret = 0

    Value = int(input("Enter radius : "))

    Ret = Circle(Value)  

    print("Area of Circle : ",Ret)

if __name__ == "__main__":
    main()    