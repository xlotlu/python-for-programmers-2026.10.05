# Write a Python program that prompts the user to enter a positive integer and
# determines whether it is a prime number. Use a for loop to check if the
# number is divisible by numbers between 1 and itself. If the number is
# divisible by any other number, break out of the loop and conclude that
# the number is not prime.
number = int(input("Enter number: "))
is_prime = True

for divisor in range(2, number):
    if number % divisor == 0:
        is_prime = False
        break

if is_prime:
    print(f"{number} is prime.")
else:
    print(f"{number} is not prime.")

# Create a Python program that prompts the user to enter a sentence and checks
# whether it meets certain criteria. Use a while loop to repeatedly prompt the
# user until a valid sentence is entered. A sentence is valid if it is longer
# than 5 characters and contains at least one space. If the input meets the
# criteria, break out of the loop.

while True:
    sentence = input("Enter sentence: ")
    if len(sentence) > 5 and " " in sentence:
        print(f'"{sentence}" is a valid sentence')
        break
