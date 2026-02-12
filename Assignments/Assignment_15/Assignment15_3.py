##################################################################################
#  Class Name :    Numbers
#  Descripton :    Performs number-related operations such as prime check,
#                  factor listing, sum of factors, and perfect number check
#  Author :        Sakshi Ashok Adale
#  Date :          11/02/2026
##################################################################################

class Numbers:
    def __init__(self,value):
        self.Value = value                # Instance Variable

    def CheckPrime(self):
        if self.Value <= 0:
            return False
        for i in range(2,int(self.Value ** 0.5) + 1):
            if self.Value % i == 0:
                return False
        return True
            
    def Factors(self):
        print("Factors are : ")
        for i in range(1,self.Value + 1):
            if self.Value % i == 0:
                print(i,end=" ")
        print()                

    def SumFactors(self):
        Sum = 0
        for i in range(1,self.Value):
            if self.Value % i == 0:
                Sum = Sum + i
        return Sum        

    def CheckPerfect(self):
        if self.SumFactors() == self.Value:
            return True
        else:
            return False         

##################################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          11/02/2026
##################################################################################

def main():
    num = int(input("Enter first number : "))
    
    obj1 = Numbers(num)

    print("Prime : ",obj1.CheckPrime())
    print("Perfect : ",obj1.CheckPerfect())
    obj1.Factors()
    print("Sum of Factors : ",obj1.SumFactors())

if __name__ == "__main__":
    main()