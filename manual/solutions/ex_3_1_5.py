# 1. Create a Python program that takes an integer input from the user and
# determines whether it is even or odd. Output "Even" if the number is
# divisible by 2, and "Odd" if it is not divisible by 2.
number = int(input("Enter number: "))
if number % 2 == 0:
    print("Even")
else:
    print("Odd")

# # 2. Ask the user to enter a password. If the input from the user is equal to
# # "pass123" display "Access granted", otherwise display "Access denied".
password = input("Enter password: ")
if password == "pass123":
    print("Access granted")
else:
    print("Access denied")

# 3. Write a Python program that determines whether a given year entered by the
# user is a leap year or not. A leap year is a year that is divisible by 4,
# but not divisible by 100 or if it is divisible by 400. Display the appropriate
# message, e.g.
#    > 2024 is a leap year
#    > 1900 is not a leap year
year = int(input("Enter year: "))
if year % 4 == 0 and not year % 100 == 0 or year % 400 == 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
