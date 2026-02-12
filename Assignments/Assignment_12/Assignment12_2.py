import threading

#############################################################################
#  Function Name : EvenFactor()
#  Descripton :    It is used to display the Even factor and their sum
#  Parameter :     Integer 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          03/02/2026
#############################################################################

def EvenFactor(No):
    evensum = 0

    for i in range(1,No+1):
        if No % i == 0 and i % 2 == 0:
            print("Even number : ",i)  
            evensum = evensum + i
    print("Sum of Even factors : ",evensum)        
             
#############################################################################
#  Function Name : OddFactor()
#  Descripton :    It is used to display the odd factor and their sum
#  Parameter :     Integer 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          03/02/2026
#############################################################################

def OddFactor(No):
    oddsum = 0

    for i in range(1,No+1):
        if No % i == 0 and i % 2 != 0:
            print("Odd number : ",i)  
            oddsum = oddsum + i
    print("Sum of Odd factors : ",oddsum)   

#############################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          03/02/2026
#############################################################################

def main():
    Value = int(input("Enter the number : "))

    t1 = threading.Thread(target=EvenFactor,args=(Value, ))
    t1.start()

    t2 = threading.Thread(target=OddFactor,args=(Value, ))
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()