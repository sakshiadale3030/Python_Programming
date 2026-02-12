import threading

#############################################################################
#  Function Name : Small()
#  Descripton :    It is used to calculate count of lowercase
#  Parameter :     Integer 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          03/02/2026
#############################################################################

def Small(str):
    count = 0

    for ch in str:
        if ch >= 'a' and ch <= 'z':
            count = count+1

    print("Number of lowercase characters : ",count)
    print("Thread Name : ",threading.current_thread().name)
    print("Thread ID : ",threading.get_ident())

#############################################################################
#  Function Name : Capital()
#  Descripton :    It is used to calculate count of uppercase
#  Parameter :     Integer 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          03/02/2026
#############################################################################

def Capital(str):
    count = 0

    for ch in str:
        if ch >= 'A' and ch <= 'Z':
            count = count + 1

    print("Number of uppercase characters : ",count) 
    print("Thread Name : ",threading.current_thread().name)
    print("Thread ID : ",threading.get_ident())       

#############################################################################
#  Function Name : Digits()
#  Descripton :    It is used to calculate count of digits
#  Parameter :     Integer 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          03/02/2026
#############################################################################

def Digits(str):
    count = 0

    for ch in str:
        if ch >= '0' and ch <= '9':
            count = count + 1
           
    print("Number of digits : ",count)
    print("Thread Name : ",threading.current_thread().name)
    print("Thread ID : ",threading.get_ident())

#############################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          03/02/2026
#############################################################################

def main():
    String = input("Enter the string : ")

    t1 = threading.Thread(target=Small,args=(String, ))
    t1.start()

    t2 = threading.Thread(target=Capital,args=(String, ))
    t2.start()

    t3 = threading.Thread(target=Digits,args=(String, ))
    t3.start()


    t1.join()
    t2.join()
    t3.join()

if __name__ == "__main__":
    main()