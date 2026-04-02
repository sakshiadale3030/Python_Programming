import sys
import os
import shutil

##################################################################################
#  FunctionName :  DirectoryRename
#  Descripton :    Copies all files from source directory to destination directory.
#                  It also traverses subdirectories and copies all files into
#                  the destination folder.
#  Input :         source (str)      - Source directory path
#                  destination (str) - Destination directory path
#  Output :        Prints copied file names
#  Author :        Sakshi Ashok Adale
#  Date :          20/02/2026
##################################################################################

def DirectoryCopy(source,destination):
    if not os.path.exists(source):
        print("Directory does not exists")
        return
    
    if not os.path.isdir(source):
        print("Given path is not directory")
        return
    
    if not os.path.exists(destination):
        os.mkdir(destination)
    
    for foldername, subfolder, filenames in os.walk(source):
        for file in filenames:
            src_file = os.path.join(foldername,file)
            dest_file = os.path.join(destination,file)

            shutil.copy(src_file,dest_file)

            print("Copied file : ",file)

##################################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          20/02/2026
##################################################################################

def main():

    if len(sys.argv) < 3:
        print("Usage: python3 DirectorySearch <Directory> <Directory>")
        return
    
    DirectoryCopy(sys.argv[1],sys.argv[2])

if __name__ == "__main__":
    main()
