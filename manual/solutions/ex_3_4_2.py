# Write a Python program that prompts the user to enter a positive integer and
# prints all odd numbers up to that integer. Use a for loop to iterate over the
# range of numbers and use the continue statement to skip even numbers.
stop = int(input("Enter number: "))
for nr in range(stop):
    if nr % 2 == 0:
        continue
    print(nr)

# Create a Python program that prompts the user to enter a sentence and displays
# the non-vowel characters in the sentence. Use a for loop to iterate over the
# characters in the sentence and use the continue statement to skip vowels.
VOWELS = "aeiouAEIOU"
sentence = input("Enter sentence: ")
for char in sentence:
    if char in VOWELS:
        continue
    print(char, end="")
