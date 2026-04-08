import psutil
from datetime import datetime

##################################################################################
# Function Name : ThreadMonitoring
# Description   : This function retrieves information about all running processes
#                 and logs their thread count, process name, and PID into a file.
# Input         : None
# Output        : Creates a file "ThreadLog.txt" containing process details
# Author        : Sakshi Ashok Adale
# Date          : 23/02/2026
##################################################################################

def ThreadMonitoring():
    with open("ThreadLog.txt", "w") as f:
        f.write("Thread Monitoring Log\n")
        f.write("Timestamp : " + str(datetime.now()) + "\n\n")

        for proc in psutil.process_iter(['pid', 'name']):
            try:
                f.write(f"Process Name : {proc.info['name']}\n")
                f.write(f"PID : {proc.info['pid']}\n")
                f.write(f"Thread Count : {proc.num_threads()}\n")
                f.write("-"*40 + "\n")
            except:
                continue    

##################################################################################
# Function Name : main
# Description   : Entry point of the program. Calls the ThreadMonitoring function
#                 to generate a log of all running processes and their thread usage.
# Input         : None
# Output        : Generates "ThreadLog.txt" file
# Author        : Sakshi Ashok Adale
# Date          : 23/02/2026
##################################################################################

def main():
    ThreadMonitoring()

if __name__ == "__main__":
    main()
