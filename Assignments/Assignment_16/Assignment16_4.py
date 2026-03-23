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

def FileContents(Filename1,FileName2):
    try:
        sobj = open(Filename1,"r")
        Data1 = sobj.read()

        dobj = open(FileName2,"r")
        Data2 = dobj.read()

        if(Data1 == Data2):
            print("Success")
        else:
            print("Failure")    

        sobj.close()
        dobj.close()

    except FileNotFoundError:
        print("Unable to open file as there is no such file")        

##################################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          17/02/2026
##################################################################################

def main():

    if len(sys.argv) < 3:
        print("Usage: python3 Assignment16_1.py <Sourcefilename> <Destinationfilename>")
        return
    
    FileContents(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()