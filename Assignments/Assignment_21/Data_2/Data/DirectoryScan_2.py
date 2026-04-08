import os

def DirectoryScanner(DirectoryName):
    print("Contents of the directory are : ")
    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("Folder Name : ",FolderName)

        for Subf in SubFolderName:
            print("SubFolder name : ",Subf)

        for fname in FileName:
            print("File name : ",fname)

def main():
    DirectoryName = input("Enter the name of directory : ")

    DirectoryScanner(DirectoryName)  

if __name__ == "__main__":
    main()    