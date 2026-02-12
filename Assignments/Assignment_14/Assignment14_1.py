#############################################################################
#  Class Name :    Demo
#  Descripton :    Demonstrates use of instance variables and methods
#  Author :        Sakshi Ashok Adale
#  Date :          11/02/2026
#############################################################################

class Demo:
    Value = 10

    def __init__(self,No1,No2):
        self.No1 = No1
        self.No2 = No2

    def Fun(self):
        print("",self.No1)
        print("",self.No2)   

    def Gun(self):
        print("",self.No1)
        print("",self.No2)   

    print("Class Variable : ",Value)                 

#############################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          11/02/2026
#############################################################################

def main():
    obj1 = Demo(11, 21)
    obj2 = Demo(51,101)

    obj1.Fun()
    obj2.Fun()
    obj1.Gun()
    obj2.Gun()

if __name__ == "__main__":
    main()