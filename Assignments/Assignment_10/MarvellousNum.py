##########################################################################
#  Function Name : ChkPrime()
#  Descripton :    It is used to check the prime number
#  Parameter :     Integer 
#  Return :        Integer
#  Author :        Sakshi Ashok Adale
#  Date :          02/02/2026
##########################################################################

def ChkPrime(No):
    if(No <= 1):
        return False

    for i in range(2,int(No**0.5) + 1):
        if(No % i == 0):
            return False
    print("Print prime number : ",No)    
    return True  

