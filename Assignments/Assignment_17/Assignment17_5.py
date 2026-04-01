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

def SearchWord(Filename,string):               
    try:
        sobj = open(Filename,"r")
        Data = sobj.read()
    
        if string in Data:
            print(f"The word '{string}' is found in '{Filename}'")
        else:
            print(f"The word '{string}' is Not found in '{Filename}'")    

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

    if len(sys.argv) < 3:
        print("Usage: python3 Assigment17_  .py <ScrFilename> string ")
        return
    
    SearchWord(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()