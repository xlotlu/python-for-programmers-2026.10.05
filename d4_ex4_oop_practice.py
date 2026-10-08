# date fiind seturile de date
# 'data/clients.json' și 'data/transactions.csv'

# 1. creați clasele
# Client și BankAccount

# Client:
# - name
# - email
# - accounts

# BankAccount:
# - id
# - overdraft
# - amount

# și implementați __init__ și __repr__


class Client:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def __repr__(self):
        return f"Client(name={self.name}, email={self.email}, accounts={self.accounts})"

class BankAccount:
    def __init__(self, id, overdraft=0):
        self.id = id
        self.overdraft = overdraft
        self.balance = 0

    def __repr__(self):
        return f"BankAccount(id={self.id}, overdraft={self.overdraft}, balance={self.balance})"

# 2. implementăm debitare și creditare pe BankAccount
#    în timp ce facem protecție ca la debitarea contului
#    să nu poată trece de limita de overdraft
#
#    def credit() --> adaugă bani
#    def debit()  --> scade bani, cu grijă la protecție

class OverdraftError(ValueError):
    def __init__(self):
        super().__init__("Amount exceeds overdraft")

class BankAccount:
    def __init__(self, id, overdraft=0):
        self.id = id
        self.overdraft = overdraft
        self.balance = 0

    def __repr__(self):
        return f"BankAccount(id={self.id}, overdraft={self.overdraft}, balance={self.balance})"

    def credit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")

        self.balance += amount

    def debit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")

        if self.balance - amount < -self.overdraft:
            raise OverdraftError()

        self.balance -= amount

# 2.bis. facem protecția de overdraft mai low-level, la nivel de assignment pe atribut

# folosim @property ca getter/setter
class Whatever:
    def __init__(self):
        self.__my_value = 0

    @property                  # getter
    def my_value(self):
        return self.__my_value

    @my_value.setter           # setter
    def my_value(self, v):
        self.__my_value = v

class BankAccount:
    def __init__(self, id, client, overdraft=0):
        self.id = id
        self.overdraft = overdraft
        self.client = client
        self.__balance = 0

    def __repr__(self):
        return f"BankAccount(id={self.id}, overdraft={self.overdraft}, balance={self.balance})"

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, amount):
        if amount < -self.overdraft:
            raise OverdraftError()
        self.__balance = amount

    def credit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")

        self.balance += amount

    def debit(self, amount):
        if amount < 0:
            raise ValueError("Amount must be positive")

        self.balance -= amount

# 3. procesăm clients

import json

CLIENT_DATA = "data/clients.json"
with open(CLIENT_DATA, encoding="utf-8") as fp:
    data = json.load(fp)

    for cl in data:
        client = Client(
            name=cl['name'],
            email=cl['email_address'],
        )

        for acc in cl['bank_accounts']:
            account = BankAccount(
                id=acc['id'],
                client=client,
                overdraft=acc['overdraft'],
            )

            # TODO:
            #client.accounts.append(account)
            # make this happen automatically
            # when a new account is created


# 4. procesăm transactions

# z. să vedem ce clienți se apropie de limita de overdraft