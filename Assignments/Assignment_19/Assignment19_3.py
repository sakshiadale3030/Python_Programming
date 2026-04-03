import sys
import os
import hashlib

##################################################################################
# Function Name : CalculateChecksum
# Description   : Calculates and returns the MD5 checksum of a given file.
# Input         : path (str)       - Path of the file
#                 blocksize (int) - Size of data block to read (default: 1024 bytes)
# Output        : Returns checksum string
# Author        : Sakshi Ashok Adale
# Date          : 22/02/2026
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
# Function Name : RemoveDuplicates
# Description   : Traverses the given directory and removes duplicate files based
#                 on their checksum values. Keeps only one copy of each file.
# Input         : directory (str) - Path of directory to scan
# Output        : Returns list of removed duplicate file paths
# Author        : Sakshi Ashok Adale
# Date          : 22/02/2026
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
# Function Name : WriteLog
# Description   : Writes the list of removed duplicate files into a log file.
# Input         : removed_files (list) - List of deleted file paths
# Output        : Creates/updates "RemovedLog.txt" with removed file details
# Author        : Sakshi Ashok Adale
# Date          : 22/02/2026
##################################################################################

def WriteLog(removed_files):
    with open("RemovedLog.txt","w") as f:
        f.write("Removed Duplicates files : \n")

        for file in removed_files:
            f.write(file + "\n")

##################################################################################
# Function Name : main
# Description   : Entry point of the application. Validates command line argument,
#                 removes duplicate files, and logs the deleted files.
# Input         : Command line argument (directory path)
# Output        : Displays usage message or generates RemovedLog.txt
# Author        : Sakshi Ashok Adale
# Date          : 22/02/2026
##################################################################################

def main():

    if len(sys.argv) != 2:
        print("Usage: python3 Assignment19_1.py <Directory>")
        return
    
    removed = RemoveDuplicates(sys.argv[1])

    WriteLog(removed)

if __name__ == "__main__":
    main()
