
import threading

#############################################################################
#  Function Name : increment()
#  Descripton :    It is used to increment the global counter variable
#                  in a thread-safe manner using a Lock
#  Parameter :     None 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          03/02/2026
#############################################################################

counter = 0

lock = threading.Lock()

def increment():
    global counter

    for i in range(1000):
        lock.acquire()

        counter = counter + 1

        lock.release()

    print("Final counter value : ",counter)   

#############################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          03/02/2026
#############################################################################

def main():
    t1 = threading.Thread(target=increment)
    
    t2 = threading.Thread(target=increment)

    t3 = threading.Thread(target=increment)
    
    t1.start()
    t2.start()
    t3.start()

    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()