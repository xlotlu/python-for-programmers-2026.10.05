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

        client.accounts.append(self)

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

def import_clients(jsonfile):
    with open(CLIENT_DATA, encoding="utf-8") as fp:
        data = json.load(fp)

        for cl in data:
            client = Client(
                name=cl['name'],
                email=cl['email_address'],
            )

            for acc in cl['bank_accounts']:
                # Note: the account is automatically associated
                # to the client when created
                account = BankAccount(
                    id=acc['id'],
                    client=client,
                    overdraft=acc['overdraft'],
                )

# am întâlnit classmethods:
# - dict.fromkeys
# - dt.datetime.now
# - dt.date.today

# folosim classmethods pt. pattern-uri
# gen constructor / factory

class MyClass:
    @classmethod
    def my_method(cls):
        print(cls)

MyClass.my_method # <-- metodă bound-uită pe clasă

# task: lipim ("izolăm") funcția de import direct pe clasă
class Client:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.accounts = []

    def __repr__(self):
        return f"Client(name={self.name}, email={self.email}, accounts={self.accounts})"

    @classmethod
    def from_dict(cls, data):
        """
        Creates and returns a new Client
        from a dictionary structure as per the database dump.
        """ # <--- dacă primul obiect dintr-o definiție este un string
        # acesta este "docstring", accesibil via __doc__

        client = cls(
            name=data['name'],
            email=data['email_address'],
        )

        for acc in data['bank_accounts']:
            # Note: the account is automatically associated
            # to the client when created
            BankAccount.from_dict(acc, client)

        return client

    @classmethod
    def import_dump(cls, jsonfile):
        clients = []

        with open(CLIENT_DATA, encoding="utf-8") as fp:
            data = json.load(fp)
            for cl in data:
                clients.append(
                    cls.from_dict(cl)
                )

        return clients

class BankAccount(BankAccount):
    @classmethod
    def from_dict(cls, dct, client):
        return cls(
            id=dct['id'],
            client=client,
            overdraft=dct['overdraft'],
        )

# staticmethod:
# util pentru o funcție obișnuită
# ce conține un algoritm intern necesar clasei noastre.
#
# putea să fie o funcție în global namespace,
# doar că are sens arhitectural să fie în namespace-ul clasei
class MyCls:
    @staticmethod
    def myfunc(x, y):
        print(x, y)

# 4. procesăm transactions

import csv

class BankAccount:
    _ALL_ACCOUNTS = {}

    OVERDRAFT_WARN = .7

    def __new__(cls, id, client, overdraft=0):
        instance = super().__new__(cls)
        # we cache the instance on the class dict
        cls._ALL_ACCOUNTS[id] = instance

        return instance

    @classmethod
    def get_by_id(cls, id):
        return cls._ALL_ACCOUNTS[id]

    def __init__(self, id, client, overdraft=0):
        self.id = id
        self.overdraft = overdraft
        self.client = client
        self.__balance = 0

        client.accounts.append(self)

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

    @property
    def warn_overdraft(self):
        return self.balance <= -self.OVERDRAFT_WARN * self.overdraft 

    @classmethod
    def from_dict(cls, dct, client):
        return cls(
            id=dct['id'],
            client=client,
            overdraft=dct['overdraft'],
        )

    @classmethod
    def import_transactions(cls, csvfile):
        with open(csvfile) as f:
            for t in csv.DictReader(f):
                id = int(t['account_id'])
                type = t['transaction_type']
                amount = float(t['amount'])

                acc = cls.get_by_id(id)
                print(acc)

                if type == 'debit':
                    acc.debit(amount)
                elif type == 'credit':
                    acc.credit(amount)
                else:
                    # this is a bug in the dataset,
                    # we should probably rollback everything
                    #raise ValueError("Warning: bad transaction type")
                    pass


TRANSACTION_DATA = "data/transactions.csv"

clients = Client.import_dump(CLIENT_DATA)
BankAccount.import_transactions(TRANSACTION_DATA)

# z. să vedem ce clienți se apropie de limita de overdraft
# iterate through clients,
# iterate through their accounts
for acc in BankAccount._ALL_ACCOUNTS.values():
    print(acc.warn_overdraft, acc)