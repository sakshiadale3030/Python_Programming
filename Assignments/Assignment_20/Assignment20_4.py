import psutil
import os
import sys
import time
import smtplib
from email.message import EmailMessage
from datetime import datetime

##################################################################################
# Function Name : CreateLogFolder
# Description   : Creates a directory if it does not already exist
# Input         : folder (str) - Folder name/path
# Output        : Creates folder if not present
# Author        : Sakshi Ashok Adale
# Date          : 23/02/2026
##################################################################################

def CreateLogFolder(folder):
    if not os.path.exists(folder):
        os.mkdir(folder)

##################################################################################
# Function Name : GetLogFile
# Description   : Generates a timestamp-based log file path inside given folder
# Input         : folder (str)
# Output        : Returns full file path of log file
# Author        : Sakshi Ashok Adale
# Date          : 23/02/2026
##################################################################################        

def GetLogFile(folder):
    CreateLogFolder(folder)

    filename = "Log_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    return os.path.join(folder, filename)

##################################################################################
# Function Name : GetProcessData
# Description   : Collects detailed information about running processes such as
#                 CPU usage, memory usage, thread count, and open files
# Input         : None
# Output        : Returns list of dictionaries containing process info
# Author        : Sakshi Ashok Adale
# Date          : 23/02/2026
##################################################################################

def GetProcessData():
    data = []

    # Iterate through all running processes
    for proc in psutil.process_iter(['pid', 'name']):
        try:
            pid = proc.info['pid']
            name = proc.info['name']

            # CPU usage percentage (interval gives more accurate reading)
            cpu = proc.cpu_percent(interval=0.1)

            # Memory usage in MB (RSS = Resident Set Size)
            memory = proc.memory_info().rss / (1024 * 1024)

            # Number of threads used by process
            threads = proc.num_threads()

            try:
                # Number of open files by process
                open_files = len(proc.open_files())

            except:
                open_files = 0

            # Store all data in dictionary format
            data.append({
                "name" : name,
                "pid" : pid,
                "cpu" : cpu,
                "memory" : memory,
                "threads" : threads,
                "open_files" : open_files
            })   

        except:
            # Skip inaccessible or terminated processes
            continue

    return data

##################################################################################
# Function Name : WriteLog
# Description   : Writes collected process data into a log file
# Input         : file (str), data (list)
# Output        : Creates log file with detailed process info
# Author        : Sakshi Ashok Adale
# Date          : 23/02/2026
##################################################################################

def WriteLog(file, data):
    with open(file, "w") as f:
        f.write("System Monitoring Log\n")
        f.write("Timestamp : " + str(datetime.now()) + "\n\n")

        # Write details of each process
        for p in data:
            f.write(f"Name : {p['name']} \n") 
            f.write(f"PID : {p['pid']} \n")
            f.write(f"CPU % : {p['cpu']} \n")
            f.write(f"Memory (RSS) : {p['memory']:.2f} \n")
            f.write(f"Threads : {p['threads']} \n")
            f.write(f"Open Files : {p['open_files']} \n")
            f.write("-" * 40 + "\n")

##################################################################################
# Function Name : CreateSummary
# Description   : Generates a summary of top processes based on CPU, memory,
#                 threads, and open files
# Input         : data (list)
# Output        : Returns formatted summary string
# Author        : Sakshi Ashok Adale
# Date          : 23/02/2026
##################################################################################

def CreateSummary(data):
    total = len(data)

    # Get top 5 processes based on different metrics
    top_cpu = sorted(data, key= lambda x: x['cpu'], reverse=True)[:5]
    top_mem = sorted(data, key= lambda x: x['memory'], reverse=True)[:5]
    top_thread = sorted(data, key= lambda x: x['threads'], reverse=True)[:5]
    top_files = sorted(data, key= lambda x: x['open_files'], reverse=True)[:5]

    summary = f"Total Processes : {total} \n\n"

    summary = summary + "Top CPU Processes : \n"
    for p in top_cpu:
        summary = summary + f"{p['name']} ({p['cpu']}%)\n"

    summary = summary + "\nTop Memory Processes : \n"
    for p in top_mem:
        summary = summary + f"{p['name']} ({p['memory']:.2f} MB)\n"

    summary = summary + "\nTop Thread Processes : \n"
    for p in top_thread:
        summary = summary + f"{p['name']} ({p['threads']})\n"       
            
    summary = summary + "\nTop Open File Processes : \n"
    for p in top_files:
        summary = summary + f"{p['name']} ({p['open_files']}\n)"     

    return summary

##################################################################################
# Function Name : SendEmail
# Description   : Sends email with summary in body and log file as attachment
# Input         : receiver (str), logfile (str), summary (str)
# Output        : Sends email
# Author        : Sakshi Ashok Adale
# Date          : 23/02/2026
##################################################################################

def SendEmail(receiver, logfile, summary):
    sender = "sakshiadale3030@gmail.com"
    password = "XYZ"

    msg = EmailMessage()
    msg['Subject'] = "System Monitoring Report"
    msg['From'] = sender
    msg['To'] = receiver

    # Add summary in email body
    msg.set_content(summary)

    # Attach log file
    with open(logfile, "rb") as f :
        msg.add_attachment(f.read(), 
                           maintype='application',
                           subtype='octet-stream',
                           filename=os.path.basename(logfile)
                           )

    # Send email using Gmail SMTP over SSL    
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)    
                     
##################################################################################
# Function Name : main
# Description   : Entry point. Takes command-line arguments:
#                 1. Log folder
#                 2. Receiver email
#                 3. Time interval (in minutes)
#                 Runs monitoring in infinite loop
# Author        : Sakshi Ashok Adale
# Date          : 23/02/2026
##################################################################################

def main():

    if len(sys.argv) != 4:
        print("Usage : python3 Assignment20_4.py <LogFolder> <Email> <Interval(min)>")
        return
    
    folder = sys.argv[1]
    receiver = sys.argv[2]
    interval = int(sys.argv[3]) * 60

    while True:
        logfile = GetLogFile(folder)

        data = GetProcessData()
        WriteLog(logfile, data)

        summary = CreateSummary(data)

        try:
            SendEmail(receiver, logfile, summary)

            print("Email Sent Successfully")

        except Exception as e:
            print("Error : ",e)

        time.sleep(interval)        

if __name__ == "__main__":
    main()
