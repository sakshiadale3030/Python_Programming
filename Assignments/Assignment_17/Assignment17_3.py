import sys

##################################################################################
#  FunctionName :  DisplayFile
#  Descripton :    Reads a given file and displays its contents line by line.
#  Input :         Filename (str) - Name of the file to read
#  Output :        Prints each line of the file on the screen.
#                  Displays an error message if the file does not exist.
#  Author :        Sakshi Ashok Adale
#  Date :          17/02/2026
##################################################################################

def DisplayFile(Filename):               
    try:
        sobj = open(Filename,"r")
    
        words = 0 

        for line in sobj:
            print(line,end="")
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
    
    DisplayFile(sys.argv[1])

if __name__ == "__main__":
    main()