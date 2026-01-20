######################################################################
#  Function Name : CheckVowel()
#  Descripton :    Check the character is vowel or not
#  Parameter :     Character
#  Return :        boolean
#  Author :        Sakshi Ashok Adale
#  Date :          19/01/2026
######################################################################

def CheckVowel(char):
    if (char == 'a' or char == 'e' or char == 'i' or char == 'o' or char == 'u' or char == 'A' or char == 'E' or char == 'I' or char == 'O' or char == 'U'):
        return True
    else:
        return False
       

######################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          19/01/2026
######################################################################

def main():
    Ret = False

    Value = input("Enter the character : ")

    Ret = CheckVowel(Value)  

    if(Ret == True):
        print("It is vowel")
    else:
        print("It is not vowel")

if __name__ == "__main__":
    main()    