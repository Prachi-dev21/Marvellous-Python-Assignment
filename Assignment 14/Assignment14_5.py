class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited ₹{amount}. New Balance: ₹{self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f"Withdrew ₹{amount}. New Balance: ₹{self.balance}")

    def display_balance(self):
        print(f"Account Holder: {self.name}")
        print(f"Account Number: {self.account_number}")
        print(f"Current Balance: ₹{self.balance}")


acc1 = BankAccount("123456789", "Alice", 10000)
acc1.display_balance()
acc1.deposit(5000)
acc1.withdraw(3000)
acc1.display_balance()

print("\n")

acc2 = BankAccount("987654321", "Bob", 2000)
acc2.display_balance()
acc2.withdraw(2500)  
acc2.deposit(1000)
acc2.display_balance()
