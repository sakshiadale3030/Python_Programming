import os

def main():
    DirectoryName = input("Enter the name of directory")

    print("Contents of the directory are : ")

    for FolderName, SubFolderName, FileName in os.walk(DirectoryName):
        print("Folder Name : ",FolderName)

        for Subf in SubFolderName:
            print("SubFolder name : ",Subf)

        for fname in FileName:
            print("File name : ",fname)

if __name__ == "__main__":
    main()    