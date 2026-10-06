# Create a program that takes the current hour as an integer value
# (in 24-hour format) as input from the user and greets them with an
# appropriate message based on the time of day:
# Morning: [5 - 12)
# Afternoon: [12 - 17)
# Evening: [17 - 21)
# Night: [21 - 5)
hour = int(input("Enter current hour: "))  # between 0 and 23
if 5 <= hour < 12:
    print("Good morning!")
elif 12 <= hour < 17:
    print("Good afternoon!")
elif 17 <= hour < 21:
    print("Good evening!")
elif hour < 24:
    print("Good night!")


# Create a program that asks the user to enter two numbers. Display the larger
# number or the message "The numbers are equal" if they are equal.
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

if first_number > second_number:
    print(f"{first_number} is the larger number.")
elif second_number > first_number:
    print(f"{second_number} is the larger number.")
else:
    print("The numbers are equal.")
