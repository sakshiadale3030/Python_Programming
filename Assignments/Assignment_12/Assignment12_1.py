import threading

#############################################################################
#  Function Name : CheckEven()
#  Descripton :    It is used to display the Even number 
#  Parameter :     Integer 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          03/02/2026
#############################################################################

def CheckEven(No):
    for i in range(2,No+1,2):
        print("Even number : ",i)   

#############################################################################
#  Function Name : CheckOdd()
#  Descripton :    It is used to display the odd number 
#  Parameter :     Integer 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          03/02/2026
#############################################################################

def CheckOdd(No):
    for i in range(1,No,2):
         print("Odd number : ",i)   

#############################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          03/02/2026
#############################################################################

def main():
    Value = int(input("Enter the number : "))

    t1 = threading.Thread(target=CheckEven,args=(Value, ))
    t1.start()

    t2 = threading.Thread(target=CheckOdd,args=(Value, ))
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()