######################################################################
#  Function Name : Square()
#  Descripton :    Square the number
#  Parameter :     one number
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          21/01/2026
######################################################################

Square = lambda No : No**2

######################################################################
#  Function Name : mapX()
#  Descripton :    It is used to map the function
#  Parameter :     one number
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          21/01/2026
######################################################################

def mapX(Task,Element):
    Result = list()

    for no in Element:
        Ret = Task(no)
        Result.append(Ret)

    return Result    
  
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          21/01/2026
######################################################################

def main():
    Ret = 0

    Size = int(input("Enter the Elements : "))
    Data = []
    for i in range(Size):
        Data.append(int(input("Enter element :")))
    print("Actual Data is : ",Data)    

    MData = list(mapX(Square, Data))
    print("Data after map is : ",MData)

if __name__ == "__main__":
    main()