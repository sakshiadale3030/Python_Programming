######################################################################
#  Function Name : Display()
#  Descripton :    It is used to display the even number
#  Parameter :     one integer 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          28/01/2026
######################################################################

def Display(No):
    for i in range(1,No+1):
        if(No % 2 == 0):
            print(i*2, end="\t")  
    
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          28/01/2026
######################################################################

def main():
    Value = int(input("Enter number : "))

    Display(Value) 

if __name__ == "__main__":
    main()