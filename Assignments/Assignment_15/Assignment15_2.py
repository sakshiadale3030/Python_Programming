##################################################################################
#  Class Name :    BankAccount
#  Descripton :    Manages bank account details and performs deposit, withdrawal,
#                  and interest calculation operations
#  Author :        Sakshi Ashok Adale
#  Date :          11/02/2026
##################################################################################

class BankAccount:
    ROI = 10.5                          # Class Variable

    def __init__(self,name,amount):
        self.Name = name                # Instance Variable
        self.Amount = amount            # Instance Variable

    def Deposit(self):
        deposit_amount = float(input("Enter the amount to deposit : "))
        self.Amount = self.Amount + deposit_amount
        print("Amount deposited successfully.")

    def Withdraw(self):
        withdraw_amount = float(input("Enter the amount to withdraw : "))
        if(withdraw_amount <= self.Amount):
            self.Amount = self.Amount - withdraw_amount
            print("WithDraw successfully")    
        else:
            print("Insufficient balance!")   

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        return interest

    def Display(self):
        print("Account Holder Name : ",self.Name)
        print("Current Balance : ",self.Amount)         

##################################################################################
# Function name :- main()
# Description :-   Entry point of the application
# Author :         Sakshi Ashok Adale
# Date :-          11/02/2026
##################################################################################

def main():
    name = input("Enter account holder name : ")
    amount = float(input("Enter initial amount : "))

    obj = BankAccount(name,amount)

    obj.Display()
    obj.Deposit()
    obj.Withdraw()
    obj.CalculateInterest()
    obj.Display()

    interest = obj.CalculateInterest()
    print("Interest on current balance : ",interest)

if __name__ == "__main__":
    main()