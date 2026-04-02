import sys
import os

##################################################################################
#  FunctionName :  DirectorySearch
#  Descripton :    Searches for files with a given extension in a directory.
#  Input :         path (str) - Directory path
#                  extension (str) - File extension to search
#  Output :        Prints matching file names
#  Author :        Sakshi Ashok Adale
#  Date :          20/02/2026
##################################################################################

def DirectorySearch(path,extension):

    path = os.path.abspath(path)

    if not os.path.exists(path):
        print("Directory does not exists")
        return
    
    if not os.path.isdir(path):
        print("Given path is not directory")
        return
    
    print("File with extension ."+ extension +" are :\n")

    for foldername, subfolder, filenames in os.walk(path):
        for file in filenames:
            if file.lower().endswith(extension.lower()):
                print(os.path.join(foldername, file))

##################################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          20/02/2026
##################################################################################

def main():

    if len(sys.argv) < 3:
        print("Usage: python3 DirectorySearch <Directory> <Extension> ")
        return
    
    DirectorySearch(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()