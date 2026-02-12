import threading

#############################################################################
#  Function Name : thread1()
#  Descripton :    It is used to display prime numner
#  Parameter :     Integer 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          03/02/2026
#############################################################################

def is_Prime(Arr):
    prime = []

    for num in Arr:
        if num <= 1:
            continue
        
        for i in range(2,num):
            if num % i == 0:
                break
        else:
            prime.append(num)   

    print("Prime number : ",prime)        

#############################################################################
#  Function Name : thread2()
#  Descripton :    It is used to display Non prime number
#  Parameter :     Integer 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          03/02/2026
#############################################################################

def is_NonPrime(Arr):
    nonprime = []

    for num in Arr:
        if num <= 1 :
            nonprime.append(num)
            continue
        
        for i in range(2,num):
            if num % i == 0:
                nonprime.append(num)
                break
            
    print("Prime number : ",nonprime)            

#############################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          03/02/2026
#############################################################################

def main():
    lst = list(map(int,input("Enter the elements : ").split()))

    t1 = threading.Thread(target=is_Prime,args=(lst,))
    
    t2 = threading.Thread(target=is_NonPrime,args=(lst,))
    
    t1.start()
    t2.start()

    t1.join()
    t2.join()

if __name__ == "__main__":
    main()