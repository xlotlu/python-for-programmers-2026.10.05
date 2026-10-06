# Write a function that takes a list of strings and an integer min_length
# (optional) as parameters and returns the list of strings longer than
# min_length. By default (when min_length not given), it should return the
# original list.
#
# E.g.
#
#  filter_strings(["hello", "", "hi", "bye"], min_length=2)
# returns ['hello', 'bye']
#  filter_strings(["hello", "", "hi", "bye"])
# returns ["hello", "", "hi", "bye"]
def filter_strings(strings, min_length=None):
    if not min_length:
        return strings

    filtered_strings = []
    for string in strings:
        if len(string) > min_length:
            filtered_strings.append(string)
    return filtered_strings


def filter_strings_v2(strings, min_length=None):
    if not min_length:
        return strings

    return [s for s in strings if len(s) > min_length]


print(filter_strings(["hello", "", "hi", "bye"], min_length=2))
print(filter_strings(["hello", "", "hi", "bye"], min_length=0))
print(filter_strings(["hello", "", "hi", "bye"]))

print(filter_strings_v2(["hello", "", "hi", "bye"], min_length=2))
print(filter_strings_v2(["hello", "", "hi", "bye"], min_length=0))
print(filter_strings_v2(["hello", "", "hi", "bye"]))


# The remove method removes the first occurrence of a value in a list. Write a
# function that removes all occurrences of a certain value.
def remove_all(list_obj, value):
    new_list = list_obj.copy()
    while value in new_list:
        new_list.remove(value)
    return new_list


numbers = [1, 2, 3, 1, 2, 8]
print(remove_all(numbers, 1))
print("Initial list remains unchanged:", numbers)
print(remove_all(numbers, 7))


# [optional] Write a function strip_all that receives two parameters: a list of
# strings strings (required) and a string chars (optional), and returns a list
# containing all items in strings with leading and trailing characters in chars
# removed. If chars is not given, it should strip whitespaces around strings.
#
# E.g.
#
# strip_all(["\nAnna", "Jane ", "  Mike\n"])  # returns ["Anna", "Jane", "Mike"]
# strip_all(["Anna;", "Jane,", ",Mike"], ",;")
# returns ["Anna", "Jane", "Mike"]

def strip_all(strings, chars=None):
    stripped_strings = []
    for string in strings:
        stripped_strings.append(string.strip(chars))
    return stripped_strings


def strip_all_v2(strings, chars=None):
    return [s.strip(chars) for s in strings]


print(strip_all(["\nAnna", "Jane ", "  Mike\n"]))
print(strip_all(["Anna;", "Jane,", ",Mike"], ",;"))

print(strip_all_v2(["\nAnna", "Jane ", "  Mike\n"]))
print(strip_all_v2(["Anna;", "Jane,", ",Mike"], ",;"))
