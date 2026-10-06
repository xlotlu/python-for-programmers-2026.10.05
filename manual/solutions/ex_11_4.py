# Modify BankAccount class to receive two parameters on initialisation:
# bank_name - a string to identify the bank (required)
# balance - a number that holds the current balance (optional, default 0)
class BankAccount:
    def __init__(self, bank_name, balance=0):
        self.bank_name = bank_name
        self.balance = balance


# Create two BankAccount instances (different bank names, one with balance
# specified, the other one without) and inspect their attributes.
bank_acc_jane = BankAccount("RandomBank", 1000)
print(bank_acc_jane.bank_name, bank_acc_jane.balance)

bank_acc_john = BankAccount("ImaginaryBank")
print(bank_acc_john.bank_name, bank_acc_john.balance)
