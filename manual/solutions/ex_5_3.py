# Write a function multiply that receives two required parameters and prints
# their product (using * operator). Call the function with the following
# arguments:
# 7 and 6.2
# "hello" and 3
# [0] and 5
# What do you notice?
def multiply(a, b):
    print(a * b)


multiply(7, 6.2)
multiply("hello", 3)
multiply([0], 5)


# Write a Python function called greet that takes an optional parameter name.
# If a name is provided, print a greeting message to that name; otherwise,
# print a generic greeting message. Call the function with and without a
# parameter.
def greet(name=None):
    if name:
        print(f"Hello, {name}!")
    else:
        print("Hi there!")


greet()
greet("Sam")


# Call the function above on each item in the following list:
names = ["Anna", "Jane", "Mike"]
for person_name in names:
    greet(person_name)
