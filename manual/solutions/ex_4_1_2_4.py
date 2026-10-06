# Iterate on the greetings list created above and print, for each item, the
# length of the string and a message saying if the string contains "good" or
# not, e.g.
# "hello" has a length of 5 characters.
# "hello" does not contain "good".
# [...]
# "good morning" has a length of 12 characters.
# "good morning" contains "good".
greetings = ["hello", "hi", "good morning", "good afternoon"]

for greeting in greetings:
    print(f'"{greeting}" has a length of {len(greeting)} characters.')
    if "good" in greeting:
        print(f'"{greeting}" contains "good".')
    else:
        print(f'"{greeting}" does not contain "good".')
    print()

# Given the following list, print all elements that have two or more elements:
list_of_lists = [
    [10, 20],
    [40],
    [30, 56, 25],
    [23, 14],
    [33],
    [],
    [40, 22, 47, 39],
]
for inner_list in list_of_lists:
    if len(inner_list) >= 2:
        print(inner_list)
