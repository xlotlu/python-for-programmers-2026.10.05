# Given the following variables
first_name = 'Mike'
last_name = 'Clarkson'
accounts = 2
balance = 128.5532
# print the following message using f-strings:
# M. Clarkson has 2 bank accounts with a total balance of 128.55$.

message = f"{first_name[0]}. {last_name} has {accounts} bank accouts with a total balance of {balance:.2f}$."
print(message)
