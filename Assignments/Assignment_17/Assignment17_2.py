import sys

##################################################################################
#  FunctionName :  CountLines
#  Descripton :    Reads a given file and counts the total number of words
#                  present in the file. Each line is split into words using
#                  whitespace as a separator, and the total count is calculated.
#  Input :         Filename (str) - Name of the file to read
#  Output :        Prints the total number of words in the file.
#                  Displays an error message if the file does not exist.
#  Author :        Sakshi Ashok Adale
#  Date :          17/02/2026
##################################################################################

def CountWords(Filename):               
    try:
        sobj = open(Filename,"r")
    
        words = 0 

        for line in sobj:
            words = words + len(line.split())
        
        print("Count of words are : ",words)

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
    
    CountWords(sys.argv[1])

if __name__ == "__main__":
    main()