######################################################################
#  Function Name : Pattern()
#  Descripton :    It is used to display the pattern
#  Parameter :     Integer 
#  Return :        Nothing
#  Author :        Sakshi Ashok Adale
#  Date :          28/01/2026
######################################################################

def Pattern(No):
    for i in range(1,No+1):
        for j in range(1,i+1):
            print(j,end=" ")
        print()    

######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          28/01/2026
######################################################################

def main():
    Value = int(input("Enter the number : "))

    Pattern(Value)

if __name__ == "__main__":
    main()