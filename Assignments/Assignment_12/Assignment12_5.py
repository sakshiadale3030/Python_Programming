import threading

#############################################################################
#  Function Name : thread1()
#  Descripton :    It is used to display number from 1 to 50
#  Parameter :     Integer 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          03/02/2026
#############################################################################

def thread1():
    print("Thread1 : ")
    for i in range(1,51):
        print(i)

#############################################################################
#  Function Name : thread2()
#  Descripton :    It is used to display number from 50 to 1
#  Parameter :     Integer 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          03/02/2026
#############################################################################

def thread2():
    print("Thread2 : ")
    for i in range(50,0,-1):
        print(i)        

#############################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          03/02/2026
#############################################################################

def main():
    t1 = threading.Thread(target=thread1)
    
    t2 = threading.Thread(target=thread2)
    
    t1.start()
    t1.join()

    t2.start()
    t2.join()

if __name__ == "__main__":
    main()