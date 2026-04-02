import sys
import os

##################################################################################
#  FunctionName :  DirectoryRename
#  Descripton :    Renames all files with a given old extension to a new extension
#                  in the specified directory (including subdirectories).
#  Input :         path (str)     - Directory path
#                  old_ext (str)  - Old file extension to search
#                  new_ext (str)  - New file extension to replace with
#  Output :        Prints matching file names
#  Author :        Sakshi Ashok Adale
#  Date :          20/02/2026
##################################################################################

def DirectoryRename(path,old_ext,new_ext):

    path = os.path.abspath(path)

    if not os.path.exists(path):
        print("Directory does not exists")
        return
    
    if not os.path.isdir(path):
        print("Given path is not directory")
        return
    
    for foldername, subfolder, filenames in os.walk(path):
        for file in filenames:
            if file.endswith("."+old_ext):
                old_name = os.path.join(foldername,file)
                new_name = os.path.join(foldername,file.replace("." + old_ext, "." + new_ext))

                os.rename(old_name,new_name)

                print("Renamed file : ",file)

##################################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          20/02/2026
##################################################################################

def main():

    if len(sys.argv) < 4:
        print("Usage: python3 DirectorySearch <Directory> <Extension> <Extension>")
        return
    
    DirectoryRename(sys.argv[1],sys.argv[2],sys.argv[3])

if __name__ == "__main__":
    main()