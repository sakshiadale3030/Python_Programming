##################################################################################
#  Class Name :    Circle
#  Descripton :    Demonstrates calculation of area and circumference of a circle
#  Author :        Sakshi Ashok Adale
#  Date :          11/02/2026
##################################################################################

class Circle:
    PI = 3.14

    def __init__(self):
        self.Radius = 0.0
        self.Area = 0.0
        self.Circumference = 0.0

    def Accept(self):
        self.Radius = float(input("Enter the radius : "))   

    def CalculateArea(self):
        self.Area = Circle.PI * self.Radius * self.Radius

    def CalculateCircumference(self):
        self.Circumference = 2 * Circle.PI * self.Radius

    def Display(self):
        print("Radius : ", self.Radius)
        print("Area : ", self.Area)
        print("Circumference : ", self.Circumference)

print("-"*50)                             

##################################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          11/02/2026
##################################################################################

def main():
    obj1 = Circle()
    obj2 = Circle()

    obj1.Accept()
    obj1.CalculateArea()
    obj1.CalculateCircumference()
    obj1.Display()

    obj2.Accept()
    obj2.CalculateArea()
    obj2.CalculateCircumference()
    obj2.Display()


if __name__ == "__main__":
    main()