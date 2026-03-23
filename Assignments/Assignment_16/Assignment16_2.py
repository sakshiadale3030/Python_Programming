import sys

##################################################################################
#  FunctionName :  FileContents
#  Descripton :    Opens a given file in read mode and prints its contents.
#  Input :         FileName (str) - Name of the file to check
#  Output :        Prints a message if the file is opened successfully and
#                  displays the contents of the file. Prints an error message
#                  if the file does not exist.
#  Author :        Sakshi Ashok Adale
#  Date :          17/02/2026
##################################################################################

def FileContents(FileName):
    try:
        fobj = open(FileName,"r")
        print("File gets successfully opened")

        Data = fobj.read()

        print("Data from file : ",Data)  

        fobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")        

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
    
    FileContents(sys.argv[1])

if __name__ == "__main__":
    main()