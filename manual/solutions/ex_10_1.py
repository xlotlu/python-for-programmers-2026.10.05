# Write a program to read two numbers: x and y from standard input and print the
# result of x / y. If the user inputs invalid data (non-numeric input or 0 for
# y), display an error message and exit gracefully.
try:
    x = int(input("Enter first number: "))
    y = int(input("Enter second number: "))
    print("Division result: ", x / y)
except ValueError:
    print("Please enter numeric values")
except ZeroDivisionError:
    print("Cannot divide by 0")


# Modify the previous program so that it asks the user to re-enter data until
# valid.

while True:
    try:
        x = int(input("Enter first number: "))
        y = int(input("Enter second number: "))
        print("Division result: ", x / y)
        break
    except ValueError:
        print("Please enter numeric values")
    except ZeroDivisionError:
        print("Cannot divide by 0")
