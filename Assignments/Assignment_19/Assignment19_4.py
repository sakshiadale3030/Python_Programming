import sys
import os
import time
import hashlib

##################################################################################
#  FunctionName :  CalculateChecksum
#  Descripton :    Copies all files from source directory to destination directory.
#                  It also traverses subdirectories and copies all files into
#                  the destination folder.
#  Input :         source (str)      - Source directory path
#                  destination (str) - Destination directory path
#  Output :        Prints copied file names
#  Author :        Sakshi Ashok Adale
#  Date :          20/02/2026
##################################################################################

def CalculateChecksum(path,blocksize=1024):
    file = open(path,'rb')
    hobj = hashlib.md5()

    buffer = file.read(blocksize)
    while len(buffer) > 0 :
        hobj.update(buffer)
        buffer = file.read(blocksize)

    file.close()
    return hobj.hexdigest()

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

def RemoveDuplicates(directory):
    duplicates = {}
    removed_files = []

    for foldername, subfolder, filenames in os.walk(directory):
        for file in filenames :
            path = os.path.join(foldername,file)

            checksum = CalculateChecksum(path)

            if checksum in duplicates:
                os.remove(path)
                removed_files.append(path)
            else:
                duplicates[checksum] = [path]

    return removed_files
        
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

def WriteLog(removed_files):
    with open("RemovedLog.txt","w") as f:
        f.write("Removed Duplicates files : \n")

        for file in removed_files:
            f.write(file + "\n")

##################################################################################
# Function Name : main
# Description   : Entry point of the program. It validates input arguments,
#                 calls duplicate removal function, logs the output, and
#                 displays execution time.
# Input         : Command line argument (directory path)
# Output        : Displays execution time on console
# Author        : Sakshi Ashok Adale
# Date          : 22/02/2026
##################################################################################

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 Assignment19_4.py <Directory>")
        return
    
    start_time = time.time()

    removed = RemoveDuplicates(sys.argv[1])

    WriteLog(removed)

    end_time = time.time()

    print("Execution Time : ",end_time-start_time, "seconds")

if __name__ == "__main__":
    main()
