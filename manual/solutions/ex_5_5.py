# Define a global variable vowels as a string containing all vowels (lowercase
# and uppercase). Write a function remove_vowels that receives a string as a
# parameter and returns the string with vowels removed. You will have to use the
# global variable inside the function. Call the function on a multiline string
# defined outside the function.
vowels = "aeiouAEIOU"


def remove_vowels(input_str):
    output_str = ""
    for char in input_str:
        if char not in vowels:
            output_str += char
    return output_str


text = """In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now."""
text_without_vowels = remove_vowels(text)
print(text_without_vowels)
