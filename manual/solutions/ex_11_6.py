from solutions.ex_11_5 import BankAccount, InsufficientFundsError


class CreditBankAccount(BankAccount):
    def __init__(self, bank_name, balance, overdraft):
        super().__init__(bank_name, balance)
        self.overdraft = overdraft

    def withdraw(self, amount):
        if amount > self.balance + self.overdraft:
            raise InsufficientFundsError("Insufficient funds.")
        self.balance -= amount


if __name__ == "__main__":
    my_account = CreditBankAccount("RandomBank", 100, 100)
    my_account.deposit(20)
    my_account.withdraw(150)
    print(my_account.bank_name, my_account.balance)

    try:
        my_account.withdraw(100)
    except InsufficientFundsError as ex:
        print(ex)
    print(my_account.bank_name, my_account.balance)
