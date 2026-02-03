######################################################################
#  Function Name : Addition()
#  Descripton :    Addition of list
#  Parameter :     Integer 
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          29/01/2026
######################################################################

def Addition(Arr):
    Sum = 0

    for i in range(len(Arr)):
        Sum = Sum + Arr[i]
    return Sum    

######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          29/01/2026
######################################################################

def main():
    Ret = 0

    Size = int(input("Enter the No of elements : "))
    Data = []
    for i in range(Size):
        Data.append(int(input("Enter the data of elements : ")))
    print("Actual Data is : ",Data)    

    Ret = Addition(Data)

    print("Addition is : ",Ret)

if __name__ == "__main__":
    main()