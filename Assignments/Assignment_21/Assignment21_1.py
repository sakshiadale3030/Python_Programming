import os
import sys
import time 
import zipfile
import smtplib
from email.message import EmailMessage
from datetime import datetime

##################################################################################
#  Function Name : CreateLogFolder
#  Description   : Creates a directory named "Logs" if it does not already exist.
#  Input         : None
#  Output        : Creates a folder "Logs" in current directory
#  Author        : Sakshi Ashok Adale
#  Date          : 23/02/2026
##################################################################################

def CreateLogFolder():
    if not os.path.exists("Logs"):
        os.mkdir("Logs")

##################################################################################
#  Function Name : CreateLogFile
#  Description   : Generates a log file with current timestamp inside Logs folder.
#  Input         : None
#  Output        : Returns the name of the created log file
#  Author        : Sakshi Ashok Adale
#  Date          : 23/02/2026
##################################################################################        
        
def CreateLogFile():
    CreateLogFolder()
    filename = "Logs/Log_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".txt"
    return filename

##################################################################################
#  Function Name : BackupDirectory
#  Description   : Creates a zip backup of the given source directory by traversing
#                  all files and excluding unwanted file extensions.
#  Input         : source (string) - path of source directory
#                  ignore_ext (list) - list of extensions to ignore
#  Output        : Returns zip file name and number of files added
#  Author        : Sakshi Ashok Adale
#  Date          : 23/02/2026
##################################################################################

def BackupDirectory(source, ignore_ext):
    if not os.path.exists(source):
        print("Source directory not found")
        return None, 0

    zipname = "Backup_" + datetime.now().strftime("%Y-%m-%d_%H-%M-%S") + ".zip"

    count = 0

    with zipfile.ZipFile(zipname, 'w') as zipf:
        for folder, subfolder, files in os.walk(source):
            for file in files:
                if any(file.endswith(ext) 
                       for ext in ignore_ext):
                    continue   

                filepath = os.path.join(folder, file)
                zipf.write(filepath)
                count = count + 1

    return zipname, count

##################################################################################
#  Function Name : WriteLog
#  Description   : Writes backup details such as start time, number of files and
#                  zip file name into a log file.
#  Input         : logfile (string) - log file name
#                  zipname (string) - backup zip file name
#                  count (int) - number of files copied
#                  start_time (datetime) - backup start time
#  Output        : Creates and writes data into log file
#  Author        : Sakshi Ashok Adale
#  Date          : 23/02/2026
##################################################################################

def WriteLog(logfile, zipname, count, start_time):
    with open(logfile, "w") as f:
        f.write("Backup Log\n")
        f.write("Start Time : " + str(start_time) + "\n")
        f.write("Files Copied : " + str(count) + "\n")
        f.write("Zip File : " + zipname + "\n")

##################################################################################
#  Function Name : SendEmail
#  Description   : Sends an email with log file and zip backup as attachments
#                  using SMTP protocol.
#  Input         : receiver (string) - receiver email address
#                  logfile (string) - log file name
#                  zipname (string) - zip file name
#  Output        : Sends email with attachments
#  Author        : Sakshi Ashok Adale
#  Date          : 23/02/2026
##################################################################################

def SendEmail(receiver, logfile, zipname):
    sender = "sakshiadale3030@gmail.com"
    password = "XYZ"

    msg = EmailMessage()
    msg['Subject'] = "Backuop Completed"
    msg['From'] = sender
    msg['To'] = receiver

    msg.set_content("Backup completed successfully.\nAttached files.")

    with open(logfile, "rb") as f:
        msg.add_attachment(f.read(), 
                           maintype = 'application',
                           subtype = 'octet-stream',
                           filename = os.path.basename(logfile)
                           )                         

    with open(zipname, "rb") as f:
        msg.add_attachment(f.read(),
                           maintype = 'application',
                           subtype = 'octet-stream',
                           filename = os.path.basename(zipname)
                           )
        
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender, password)
        smtp.send_message(msg)

##################################################################################
#  Function Name : RestoreBackup
#  Description   : Extracts the given zip file into the specified destination
#                  directory.
#  Input         : zipfile_name (string) - zip file to extract
#                  destination (string) - destination directory
#  Output        : Extracts files to destination folder
#  Author        : Sakshi Ashok Adale
#  Date          : 23/02/2026
##################################################################################

def RestoreBackup(zipfile_name, destination):
    if not os.path.exists(destination):
        os.mkdir(destination)

    with zipfile.ZipFile(zipfile_name, 'r') as zipf:
        zipf.extractall(destination)

    print("Backup Restored Successfully")

##################################################################################
#  Function Name : UpdateHistory
#  Description   : Stores backup details such as timestamp, file count and zip
#                  name into History.txt file.
#  Input         : zipname (string) - zip file name
#                  count (int) - number of files
#  Output        : Updates History.txt file
#  Author        : Sakshi Ashok Adale
#  Date          : 23/02/2026
##################################################################################    

def UpdateHistory(zipname, count):
    with open("History.txt", "a") as f:
        f.write(f"{datetime.now()} | Files: {count} | Zip: {zipname}\n") 

##################################################################################
#  Function Name : ShowHistory
#  Description   : Displays all previous backup records stored in History.txt.
#  Input         : None
#  Output        : Prints history data on console
#  Author        : Sakshi Ashok Adale
#  Date          : 23/02/2026
##################################################################################        

def ShowHistory():
    if not os.path.exists("History.txt"):
        print("No history found")
        return

    with open("History.txt", "r") as f:
        print(f.read())    
                    
##################################################################################
#  Function Name : main
#  Description   : Entry point of the program. Handles backup, restore and history
#                  operations based on command line arguments.
#  Input         : Command line arguments
#  Output        : Performs backup, restore, email sending and history display
#  Author        : Sakshi Ashok Adale
#  Date          : 23/02/2026
##################################################################################

def main():
    if len(sys.argv) == 4 and sys.argv[1] == "--restore":
        RestoreBackup(sys.argv[2], sys.argv[3])
        return
    
    if len(sys.argv) == 2 and sys.argv[1] == "--history":
        ShowHistory()
        return
    
    if len(sys.argv) < 3:
        print("Usage : python3 Assignment21_1.py <SourceDir> <Email>")
        print("Restore : python3 Assignment21_1.py --restore <ZipFile> <Destination>")
        print("History : python3 Assignmnet21_1.py --history")
        return
    
    source = sys.argv[1]
    receiver = sys.argv[2]

    ignore_ext = [".tmp", ".log", ".exe"]

    start_time = datetime.now()

    logfile = CreateLogFile()
    zipname, count = BackupDirectory(source, ignore_ext)

    if zipname is None:
        return
    
    WriteLog(logfile, zipname, count, start_time)

    UpdateHistory(zipname, count)

    try:
        SendEmail(receiver, logfile, zipname)
        print("Email Sent Successfully")
    except Exception as e:
        print("Email Error : ",e)    

if __name__ == "__main__":
    main()
