########################################################################
#  Class Name :    Arithematic
#  Descripton :    Performs basic arithmetic operations on two numbers
#  Author :        Sakshi Ashok Adale
#  Date :          11/02/2026
########################################################################

class Arithematic:
    def __init__(self):
        self.Value1 = 0
        self.Value2 = 0

    def Accept(self):
        self.Value1 = int(input("Enter the first number : "))
        self.Value2 = int(input("Enter the second number : "))   

    def Addition(self):
        return self.Value1 + self.Value2

    def Substraction(self):
        return self.Value1 - self.Value2
    
    def Division(self):
        return self.Value1 / self.Value2                          

########################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          11/02/2026
########################################################################

def main():
    obj1 = Arithematic()

    obj1.Accept()
    print("Addition is : ",obj1.Addition())
    print("Substraction is : ",obj1.Substraction())
    print("Division is : ",obj1.Division())

    obj2 = Arithematic()
    obj2.Accept()
    print("Addition is : ",obj2.Addition())
    print("Substraction is : ",obj2.Substraction())
    print("Division is : ",obj2.Division())

if __name__ == "__main__":
    main()