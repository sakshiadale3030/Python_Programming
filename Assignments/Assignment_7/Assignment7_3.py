######################################################################
#  Function Name : Odd()
#  Descripton :    Search the Odd number
#  Parameter :     one number
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          22/01/2026
######################################################################

Odd = lambda No : (No % 2 != 0)

######################################################################
#  Function Name : filterX()
#  Descripton :    It is used to filter the function
#  Parameter :     one number
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          22/01/2026
######################################################################

def filterX(Task,Element):
    Result = list()

    for no in Element:
        Ret = Task(no)
        
        if(Ret == True):
            Result.append(no)

    return Result    
  
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          22/01/2026
######################################################################

def main():
    Ret = 0

    Size = int(input("Enter the Elements : "))
    Data = []
    for i in range(Size):
        Data.append(int(input("Enter element :")))
    print("Actual Data is : ",Data)    

    FData = list(filterX(Odd, Data))
    print("Data after filter is : ",FData)

if __name__ == "__main__":
    main()