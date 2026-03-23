import sys

##################################################################################
#  FunctionName :  FileCopy
#  Descripton :    Copies the contents of a source file to a destination file.
#                   Opens the source file in read mode, reads its content, and 
#                   writes it to the destination file. Prints messages indicating 
#                   success or failure.
#  Input :         FSrcFilename (str)  - Name of the source file to copy
#                   DestFileName (str) - Name of the destination file
#  Output :        Prints messages for successful copy or file not found error
#  Author :        Sakshi Ashok Adale
#  Date :          17/02/2026
##################################################################################

def FileCopy(SrcFilename,DestFileName):
    try:
        sobj = open(SrcFilename,"r")
        print("File gets successfully opened")

        Data = sobj.read()

        dobj = open(DestFileName,"w")
        dobj.write(Data)

        print("File gets copied successful")

        sobj.close()
        dobj.close()

    except FileNotFoundError:
        print("Unable to open source file: No such file exists")        

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
    
    FileCopy(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()