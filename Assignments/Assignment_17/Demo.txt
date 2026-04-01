import sys
import os

##################################################################################
#  FunctionName :  FileExists
#  Descripton :    Checks if a given file exists in the current directory.
#  Input :         FileName (str) - Name of the file to check
#  Output :        Prints whether the file exists or not
#  Author :        Sakshi Ashok Adale
#  Date :          17/02/2026
##################################################################################

def FileExists(FileName):
    Ret = os.path.exists(FileName)

    if(Ret == True):
        print("File Exists in current Directory")
    else:
        print("File does not exists in current directory")    

##################################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          17/02/2026
##################################################################################

def main():

    if len(sys.argv) < 2:
        print("Usage: python3 Assignment16_1.py <filename>")
        return
    
    FileExists(sys.argv[1])

if __name__ == "__main__":
    main()