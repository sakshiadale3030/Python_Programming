######################################################################
#  Function Name : Length()
#  Descripton :    It is used to display the length of String
#  Parameter :     String 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          28/01/2026
######################################################################

def Length(str):
    print(len(str))  
    
######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          28/01/2026
######################################################################

def main():
    String = input("Enter the String : ")

    Length(String) 

if __name__ == "__main__":
    main()