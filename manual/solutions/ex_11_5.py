class InsufficientFundsError(Exception):
    pass


class BankAccount:
    def __init__(self, bank_name, balance=0):
        self.bank_name = bank_name
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            raise InsufficientFundsError("Insufficient funds.")
        self.balance -= amount


if __name__ == "__main__":
    my_account = BankAccount("RandomBank", 100)
    my_account.withdraw(50)
    my_account.deposit(20)
    print(my_account.bank_name, my_account.balance)

    my_friends_account = BankAccount("ImaginaryBank")
    try:
        my_friends_account.withdraw(100)
    except InsufficientFundsError as ex:
        print(ex)
