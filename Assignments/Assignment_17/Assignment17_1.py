import sys

##################################################################################
#  FunctionName :  CountLines
#  Descripton :    Reads a given file and counts the total number of lines 
#                  present in the file.
#  Input :         Filename (str) - Name of the file to read
#  Output :        Prints the total number of lines in the file
#                  Displays an error message if the file does not exist
#  Author :        Sakshi Ashok Adale
#  Date :          17/02/2026
##################################################################################

def CountLines(Filename):               
    try:
        sobj = open(Filename,"r")
        
        Count = 0

        for line in sobj:
            Count = Count + 1
        
        print("Count of Lines are : ",Count)

        sobj.close()

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
        print("Usage: python3 Assigment17_  .py <Filename>")
        return
    
    CountLines(sys.argv[1])

if __name__ == "__main__":
    main()