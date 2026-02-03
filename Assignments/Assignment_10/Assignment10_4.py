##########################################################################
#  Function Name : Frequency()
#  Descripton :    It is used to search the frequency of number from list
#  Parameter :     Integer 
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          02/02/2026
##########################################################################

def Frequency(Arr,No):
    Count = 0

    for i in Arr:
        if(i == No):
            Count = Count + 1
    return Count    

##########################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          02/02/2026
##########################################################################

def main():
    Ret = 0

    Size = int(input("Enter the No of elements : "))
    Data = []
    for i in range(Size):
        Data.append(int(input("Enter the data of elements : ")))
    print("Actual Data is : ",Data)    

    Value = int(input("Enter the element to search : "))

    Ret = Frequency(Data,Value)

    print("Frequency of number from list : ",Ret)

if __name__ == "__main__":
    main()