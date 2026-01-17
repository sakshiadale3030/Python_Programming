######################################################################
#  Function Name : Summation()
#  Descripton :    Display the Summation of given number
#  Parameter :     one number
#  Return :        sum of number
#  Author :        Sakshi Ashok Adale
#  Date :          17/01/2026
######################################################################

def Summation(No):
    Sum = 0

    for i in range(1,No+1):
        Sum = Sum + i

    return Sum    

######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          17/01/2026
######################################################################

def main():
    Value = int(input("Enter number : "))

    Ret = Summation(Value)  

    print("Summation of number : ",Ret)  

if __name__ == "__main__":
    main()    