# Create two variables, single_quote_string and double_quote_string, each
# containing the same string, but enclosed with different quotation mark
# symbols. Compare the two variables (using ==, an operator which verifies
# if two values are equal). Are the two strings equal?
single_quote_string = 'hello'
double_quote_string = "hello"
print(single_quote_string == double_quote_string)
print()

# Create a multiline string (using triple quotes) containing the lyrics of a
# song you like (choose a few lines). Print the string.
lyrics = """Keep me searching
For a heart of gold
You keep me searching
And I'm growing old"""
print(lyrics)
print()

# Do the same as the previous exercise, but this time use newline characters
# inside a single line string. Which option was easier to write?
lyrics = """Keep me searching\nFor a heart of gold\nYou keep me searching\nAnd I'm growing old"""
print(lyrics)
print()

# Create a string that outputs, when printed, the following text. Use newlines
# (between lines) and tabs (after the : symbol).
# name:	Anna
# age:	20
# hobby:	writing
print("name:\tAnna\nage:\t20\nhobby:\twriting")
