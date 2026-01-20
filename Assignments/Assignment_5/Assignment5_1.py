######################################################################
#  Function Name : Rectangle()
#  Descripton :    Calculate the area of rectangle
#  Parameter :     one number
#  Return :        Area
#  Author :        Sakshi Ashok Adale
#  Date :          19/01/2026
######################################################################

def Rectangle(Length,Width):
   Area = 0

   Area = Length * Width

   return Area
    
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          19/01/2026
######################################################################

def main():
    Ret = 0

    Value1 = int(input("Enter Length : "))
    Value2 = int(input("Enter Width : "))

    Ret = Rectangle(Value1,Value2)  

    print("Area of Rectangle : ",Ret)

if __name__ == "__main__":
    main()    