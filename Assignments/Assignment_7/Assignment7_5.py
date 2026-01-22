######################################################################
#  Function Name : Maximum()
#  Descripton :    Find the Maximum
#  Parameter :     one number
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          22/01/2026
######################################################################

Maximum = lambda No1, No2 : No1 if No1 > No2 else No2

######################################################################
#  Function Name : reduceX()
#  Descripton :    It is used to reduce the function
#  Parameter :     one number
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          22/01/2026
######################################################################

def reduceX(Task,Element):
    Sum = 0

    for no in Element:
        Sum = Task(Sum,no)
        
    return Sum    
  
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

    RData = reduceX(Maximum, Data)
    print("Data after reduce is : ",RData)

if __name__ == "__main__":
    main()