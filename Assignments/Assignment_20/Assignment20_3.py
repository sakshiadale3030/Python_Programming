import psutil
from datetime import datetime

##################################################################################
#  Function Name : MemoryMonitoring
#  Description   : Collects memory usage of all running processes, sorts them in
#                  descending order, and logs the top 10 memory-consuming processes
#                  into a file.
#  Input         : None
#  Output        : Creates "MemoryLog.txt" with process memory details
#  Author        : Sakshi Ashok Adale
#  Date          : 23/02/2026
##################################################################################

def MemoryMonitoring():
    # List to store process details (name, pid, memory usage)
    process_list = []

    # Iterate through all running processes
    for proc in psutil.process_iter(['pid', 'name', 'memory_info']):
        try:
            # Extract process ID and name
            pid = proc.info['pid']
            name = proc.info['name']

            # Get memory usage in MB (RSS = Resident Set Size)
            memory = proc.info['memory_info'].rss / (1024 * 1024)

            # Append process details as a tuple
            process_list.append((name,pid,memory))

        except:
            # Skip processes that cannot be accessed
            continue

    # Sort processes by memory usage in descending order        
    process_list.sort(key=lambda x: x[2], reverse=True)

    try:
        with open("MemoryLog.txt","w") as f:
            f.write("Memory Monitoring Log\n")

            f.write("Timestamp: " + str(datetime.now()) + "\n\n")

            # Write top 10 memory-consuming processes
            for proc in process_list[:10]:
                f.write(f"Process Name : {proc[0]}\n")
                f.write(f"PID : {proc[1]}\n")
                f.write(f"Memory (MB) : {proc[2]:.2f}\n")
                f.write("-"*40 + "\n")

        print("Log file created successfully")

    except Exception as e:
        print("Error writing log file:",e)
                    
##################################################################################
# Function Name : main
# Description   : Entry point of the program. Calls MemoryMonitoring function
#                 to generate memory usage log.
# Input         : None
# Output        : Executes monitoring and creates log file
# Author        : Sakshi Ashok Adale
# Date          : 23/02/2026
##################################################################################

def main():
    MemoryMonitoring()

if __name__ == "__main__":
    main()
