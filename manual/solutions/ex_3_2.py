# Write a program that prints all integers between 500 and 525 (both included)
# using a while loop.
number1 = 500
while number1 <= 525:
    print(number1)
    number1 += 1

# Write a program that prints all numbers between 0 (included) and 100
# (not included) which are divisible by 7 but not divisible by 5.
number2 = 0
while number2 < 100:
    if number2 % 7 == 0 and not number2 % 5 == 0:
        print(number2, end=" ")
    number2 += 1
print()

for nr in range(0, 100, 7):
    if nr % 5 != 0:
        print(nr, end=" ")
print()

# Write a Python program that calculates the factorial of a given number
# entered by the user. The factorial of a non-negative integer n is the
# product of all positive integers less than or equal to n.
number3 = int(input("Enter number: "))
current_number = 1
factorial = 1

while current_number <= number3:
    factorial *= current_number
    current_number += 1

print(f"{number3}! = {factorial}")

# Create a Python program that asks the user to enter a password and continues
# prompting until they enter the correct password. The correct password is
# "password123".
password = None
CORRECT_PASSWORD = "password123"

while password != CORRECT_PASSWORD:
    password = input("Enter password: ")

print("Correct password entered.")


while True:
    password = input("Enter password: ")
    if password == CORRECT_PASSWORD:
        print("Correct password entered.")
        break
