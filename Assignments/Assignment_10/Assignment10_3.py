######################################################################
#  Function Name : Minimum()
#  Descripton :    It is used to find the Minimum number in the list
#  Parameter :     Integer 
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          02/02/2026
######################################################################

def Minimum(Arr):
    Min = Arr[0]

    for i in Arr:
        if(i < Min):
            Min = i
    return Min     

######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          02/02/2026
######################################################################

def main():
    Ret = 0

    Size = int(input("Enter the No of elements : "))
    Data = []
    for i in range(Size):
        Data.append(int(input("Enter the data of elements : ")))
    print("Actual Data is : ",Data)    

    Ret = Minimum(Data)

    print("Minimum number is : ",Ret)

if __name__ == "__main__":
    main()