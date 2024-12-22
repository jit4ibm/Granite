class BankAccount:
    def __init__(self, balance):
        self.__balance = balance  # Private variable

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("Invalid deposit amount!")

    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
        else:
            print("Invalid or insufficient funds!")

    def get_balance(self):  # Public method to access private variable
        return self.__balance

# Using encapsulation
account = BankAccount(1000)
account.deposit(500)
print("Balance:", account.get_balance())
account.withdraw(200)
print("Balance:", account.get_balance())