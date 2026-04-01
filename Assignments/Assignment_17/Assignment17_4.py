import sys

##################################################################################
#  FunctionName :  DisplayFile
#  Descripton :    Copies the contents of a source file into a destination file.
#                  The source file is opened in read mode, its contents are read,
#                  and then written into the destination file opened in write mode.
#  Input :         ScrFilename (str)  - Name of the source file
#                  DestFilename (str) - Name of the destination file
#  Output :        Displays a success message after copying.
#                  Displays an error message if the source file does not exist.
#  Author :        Sakshi Ashok Adale
#  Date :          17/02/2026
##################################################################################

def FileCopy(ScrFilename,DestFilename):               
    try:
        sobj = open(ScrFilename,"r")
        Data1 = sobj.read()
    
        dobj = open(DestFilename,"w")
        dobj.write(Data1)

        sobj.close()
        dobj.close()

        print("File gets successfully copied")

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
        print("Usage: python3 Assigment17_  .py <ScrFilename> <DestFilename> ")
        return
    
    FileCopy(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()