# Prompt the user to enter a word. Iterate over the word and display, for each
# letter, if it is a vowel or not (use vowels = "aeiouAEIOU"), e.g.
# w is not a vowel
# o is a vowel

VOWELS = "aeiouAEIOU"
word = input("Enter word: ")

for char in word:
    if char in VOWELS:
        print(f"{char} is a vowel")
    else:
        print(f"{char} is not a vowel")
