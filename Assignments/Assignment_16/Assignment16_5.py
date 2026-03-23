import sys

##################################################################################
#  FunctionName :  CountStringFrequency
#  Descripton :    Reads the contents of a given file and counts the frequency
#                  of a specified string in that file. The file content is 
#                  split into words, and the occurrence of the given string 
#                  is calculated.
#  Input :         Filename (str) - Name of the file to read
#                  string (str)   - Word whose frequency is to be counted
#  Output :        Prints the frequency of the specified string
#                  Displays an error message if the file does not exist
#  Author :        Sakshi Ashok Adale
#  Date :          17/02/2026
##################################################################################

def CountStringFrequency(Filename,string):
    try:
        sobj = open(Filename,"r")
        Data = sobj.read()

        Count = Data.count(string)
        print(f"Frequency of {string} is : ",Count)

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
        print("Usage: python3 Assigment16_5.py <Filename> String")
        return
    
    CountStringFrequency(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()