import psutil
import os
from datetime import datetime

##################################################################################
#  Function Name : OpenFileMonitoring
#  Description   : Creates a log file that contains details of all running processes
#                  and the number of files currently opened by each process.
#  Input         : None
#  Output        : Creates "OpenFileLog.txt" with process details
#  Author        : Sakshi Ashok Adale
#  Date          : 23/02/2026
##################################################################################

def OpenFileMonitoring():
    try:
        # Open log file in write mode (overwrites if already exists)
        with open("OpenFileLog.txt", "w") as f:

            # Write header information into the file
            f.write("Open Files Monitoring Log\n")
            f.write("Timestamp : " + str(datetime.now()) + "\n\n")

            # Iterate through all running processes
            for proc in psutil.process_iter(['pid', 'name']):
                try:
                    pid = proc.info['pid']
                    name = proc.info['name']

                    try:
                        # Get list of files opened by the process
                        files = proc.open_files()

                        count = len(files)

                    except(psutil.AccessDenied,psutil.NoSuchProcess):
                        # Handle cases where access is denied or process no longer exists
                        count = "Access Denied"

                    # Write process details into log file
                    f.write(f"Process Name : {name}\n")
                    f.write(f"PID : {pid}\n")
                    f.write(f"Open Files : {count}\n")
                    f.write("-"*40 + "\n")
                except(psutil.NoSuchProcess,psutil.AccessDenied,psutil.ZombieProcess):
                    continue    

            print("Log file created successfully")  

    except Exception as e:
        print("Error : ",e)          

##################################################################################
# Function Name : main
# Description   : Entry point of the program. Calls the OpenFileMonitoring function.
# Input         : None
# Output        : Executes monitoring and creates log file
# Author        : Sakshi Ashok Adale
# Date          : 23/02/2026
##################################################################################

def main():
    OpenFileMonitoring()

if __name__ == "__main__":
    main()
