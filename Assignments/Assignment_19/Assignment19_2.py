import sys
import os
import hashlib

##################################################################################
# Function Name : CalculateChecksum
# Description   : Calculates and returns the MD5 checksum of a given file.
# Input         : path (str) - Path of the file
#                 blocksize (int) - Size of each read block (default: 1024 bytes)
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
# Function Name : FindDuplicates
# Description   : Traverses the given directory and identifies duplicate files
#                 based on their checksum values.
# Input         : directory (str) - Path of directory to scan
# Output        : Returns dictionary where:
#                 key   = checksum
#                 value = list of file paths with same checksum
# Author        : Sakshi Ashok Adale
# Date          : 22/02/2026
##################################################################################

def FindDuplicates(directory):
    duplicates = {}

    for foldername, subfolder, filenames in os.walk(directory):
        for file in filenames :
            path = os.path.join(foldername,file)

            checksum = CalculateChecksum(path)

            if checksum in duplicates:
                duplicates[checksum].append(path)

            else:
                duplicates[checksum] = [path]

    return duplicates
        
##################################################################################
# Function Name : WriteLog
# Description   : Writes duplicate file information into a log file.
# Input         : duplicates (dict) - Dictionary containing checksum and file paths
# Output        : Creates/updates "Log.txt" file with duplicate file details
# Author        : Sakshi Ashok Adale
# Date          : 22/02/2026
##################################################################################

def WriteLog(duplicates):
    with open("DuplicateLog.txt","w") as f:
        for checksum, files in duplicates.items():
            if len(files) > 1 :
                f.write("Duplicate files : \n")

                for file in files:
                    f.write(file + "\n")

                f.write("\n")         
            
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
    
    duplicates = FindDuplicates(sys.argv[1])

    WriteLog(duplicates)

if __name__ == "__main__":
    main()