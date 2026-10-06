# Ask the user to input a number and store it in a float variable.
# Write expressions that check the following:
# if the number is equal to 5
# if the number is different than 3
# if the number is greater than or equal to 0
# if the number is strictly greater than 4.3 and smaller or equal to 7.9
number = float(input("Enter a number: "))
print(number == 5)
print(number != 3)
print(number >= 0)
print(4.3 < number <= 7.9)

# Ask the user to input their name. Write an expression that is True if the name
# is longer than 5 characters.
name = input("Enter your name: ")
print(len(name) > 5)

# Ask the user to input a word. Check if that word is a palindrome
# (the word is the same if read the same backwards as forwards, e.g. "madam").
word = input("Enter a word: ")
print(word == word[::-1])
