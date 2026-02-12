import threading

#############################################################################
#  Function Name : EvenList()
#  Descripton :    It is used to display the Even list and their sum
#  Parameter :     Integer 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          03/02/2026
#############################################################################

def EvenList(Arr):
    evensum = 0
    even_list = []

    for i in Arr:
        if i % 2 == 0:
            even_list.append(i)
            evensum = evensum + i

    print("Even number : ",even_list)         
    print("Sum of Even factors : ",evensum)        
             
#############################################################################
#  Function Name : OddList()
#  Descripton :    It is used to display the odd list and their sum
#  Parameter :     Integer 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          03/02/2026
#############################################################################

def OddList(Arr):
    oddsum = 0
    odd_list = []

    for i in Arr:
        if i % 2 != 0:
            odd_list.append(i)
            oddsum = oddsum + i
            
    print("Odd number : ",odd_list)          
    print("Sum of Odd factors : ",oddsum)   

#############################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          03/02/2026
#############################################################################

def main():
    lst = list(map(int,input("Enter the elements : ").split()))

    t1 = threading.Thread(target=EvenList,args=(lst, ))
    t1.start()

    t2 = threading.Thread(target=OddList,args=(lst, ))
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()