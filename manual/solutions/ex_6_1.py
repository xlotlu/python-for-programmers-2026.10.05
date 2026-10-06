# Write a function get_words which receives a string as a parameter and does the following:
#
# removes punctuation marks (,, ., ! and ?)
# transforms everything to lowercase
# splits the string by space
# returns the list of words
# Call the function on a sentence like One warm, sunny day Jessica and Lilly
# went to the Zoo. When they arrived, they visited the monkeys.
PUNCTUATION_MARKS = ",.?!:;()"


def get_words(sentence):
    for mark in PUNCTUATION_MARKS:
        sentence = sentence.replace(mark, "")
    sentence = sentence.lower()
    return sentence.split()


my_sentence = ("One warm, sunny day Jessica and Lilly went to the Zoo. "
               "When they arrived, they visited the monkeys.")
words = get_words(my_sentence)
print(words)


# Write a function called validate_password that validates a password based on
# certain criteria:
# the password has at least 8 characters
# the password contains at least one uppercase letter
# the password contains at least one lowercase letter
# the password contains at least one digit.
# If all criteria are met, return True; otherwise, return False.

def validate_password(password):
    if len(password) < 8:
        return False

    contains_uppercase = False
    contains_lowercase = False
    contains_digit = False

    for char in password:
        if char.isupper():
            contains_uppercase = True
        elif char.islower():
            contains_lowercase = True
        elif char.isdigit():
            contains_digit = True

        if contains_uppercase and contains_lowercase and contains_digit:
            return True

    return False


print(validate_password(""))
print(validate_password("short"))
print(validate_password("UPPER1234"))
print(validate_password("lower1234"))
print(validate_password("12345678"))
print(validate_password("NoDigits"))
print(validate_password("Pass1234"))
print(validate_password("Pass1234#!"))
print(validate_password("Pa1ss1234#!awefscxhjwrw3485y3uquretweh"))
