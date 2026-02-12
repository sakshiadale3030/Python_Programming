
import threading

#############################################################################
#  Function Name : Maximum()
#  Descripton :    It is used to display maximum number from the list
#  Parameter :     Integer 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          03/02/2026
#############################################################################

def Maximum(Arr):
    Max = Arr[0]

    for num in Arr:
        if num > Max:
            Max = num
            
    print("Maximum number is : ",Max)

#############################################################################
#  Function Name : Minimum()
#  Descripton :    It is used to display minimum number from the list
#  Parameter :     Integer 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          03/02/2026
#############################################################################

def Minimum(Arr):
    Min = Arr[0]

    for num in Arr:
        if num < Min :
            Min = num
                     
    print("Minimum number is : ",Min)

#############################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          03/02/2026
#############################################################################

def main():
    lst = list(map(int,input("Enter the elements : ").split()))

    t1 = threading.Thread(target=Maximum,args=(lst,))
    
    t2 = threading.Thread(target=Minimum,args=(lst,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()