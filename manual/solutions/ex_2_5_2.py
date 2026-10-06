# Store the following strings in different variables and check if any one of
# them is contained in "The Zen of Python":
title = "The Zen of Python"
zen = "zen"
python = "Python"
empty_str = ""
print(zen in title)
print(python in title)
print(empty_str in title)

# Following the images below for guidance, build and print your first name
# initial with ASCII art. You will have to use string concatenation and
# multiplication.
letter_i = 5 * "I" + 5 * ("\n" + 2 * " " + "I" + 2 * " ") + "\n" + 5 * "I"
print(letter_i)

# Given the string "abcdefghijklmn" print the following:
my_string = "abcdefghijklmn"
# the third character of this string.
print(my_string[2])
# the second to last character of this string.
print(my_string[-2])
# the first five characters of this string.
print(my_string[:5])
# all but the last two characters of this string.
print(my_string[:-2])
# all the characters of this string with even indices (remember indexing starts
# at 0, so the characters are displayed starting with the first).
print(my_string[::2])
# all the characters of this string with odd indices (i.e. starting with the
# second character in the string).
print(my_string[1::2])
# all the characters of the string in reverse order.
print(my_string[::-1])
# every second character of the string in reverse order, starting from the last
# one.
print(my_string[::-2])
