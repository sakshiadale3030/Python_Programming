##################################################################################
#  Class Name :    BookStore
#  Descripton :    Maintains book details and counts the total number of books
#  Author :        Sakshi Ashok Adale
#  Date :          11/02/2026
##################################################################################

class BookStore:
    NoOfBooks = 0

    def __init__(self,BookName,Author):
        self.BookName = BookName
        self.Author = Author
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(self.BookName,"by",self.Author,".","No of Books : ",BookStore.NoOfBooks)

##################################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          11/02/2026
##################################################################################

def main():
    obj1 = BookStore("Linux System Programming", "Robert Love")
    obj1.Display()

    obj2 = BookStore("C Programming", "Dennis Ritchie")
    obj2.Display()

if __name__ == "__main__":
    main()