class BankAccount:
    
    ROI = 10.5

  
    def __init__(self):
        self.Name = input("Enter account holder name: ")
        self.Amount = float(input("Enter initial account balance: "))

    
    def Deposit(self):
        deposit_amt = float(input(f"{self.Name}, enter amount to deposit: "))
        self.Amount += deposit_amt
        print(f"Deposited {deposit_amt}. Updated balance: {self.Amount}")

    
    def Withdraw(self):
        withdraw_amt = float(input(f"{self.Name}, enter amount to withdraw: "))
        if withdraw_amt <= self.Amount:
            self.Amount -= withdraw_amt
            print(f"Withdrawn {withdraw_amt}. Updated balance: {self.Amount}")
        else:
            print("Insufficient balance!")

    def CalculateInterest(self):
        interest = (self.Amount * BankAccount.ROI) / 100
        print(f"Interest on current balance at ROI {BankAccount.ROI}%: {interest}")

    
    def Display(self):
        print(f"Account Holder: {self.Name}")
        print(f"Current Balance: {self.Amount}")



def main():
    print("First Account ")
    acc1 = BankAccount()
    acc1.Display()
    acc1.Deposit()
    acc1.Withdraw()
    acc1.CalculateInterest()
    acc1.Display()

    print("\nSecond Account ")
    acc2 = BankAccount()
    acc2.Display()
    acc2.Deposit()
    acc2.Withdraw()
    acc2.CalculateInterest()
    acc2.Display()


if __name__ == "__main__":
    main()
