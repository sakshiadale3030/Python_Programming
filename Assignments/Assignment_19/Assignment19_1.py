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
# Function Name : DirectoryChecksum
# Description   : Traverses the given directory and calculates checksum of each
#                 file. It also processes all subdirectories recursively.
# Input         : directory (str) - Path of directory to scan
# Output        : Prints file name along with its checksum
# Author        : Sakshi Ashok Adale
# Date          : 22/02/2026
##################################################################################

def DirectoryChecksum(directory):
    if not os.path.exists(directory):
        print("Directory does not exists")
        return
    
    for foldername, subfolder, filenames in os.walk(directory):
        for file in filenames:
            path = os.path.join(foldername,file)

            checksum = CalculateChecksum(path)

            print(f"{file} : {checksum}")
            
##################################################################################
# Function Name : main
# Description   : Entry point of the application. Validates command line argument
#                 and initiates directory checksum process.
# Input         : Command line argument (directory path)
# Output        : Displays usage message or prints checksum of files
# Author        : Sakshi Ashok Adale
# Date          : 22/02/2026
##################################################################################


def main():

    if len(sys.argv) != 2:
        print("Usage: python3 Assignment19_1.py <Directory>")
        return
    
    DirectoryChecksum(sys.argv[1])

if __name__ == "__main__":
    main()