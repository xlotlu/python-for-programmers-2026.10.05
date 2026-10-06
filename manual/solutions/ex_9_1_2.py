# Using the person dictionary above:
# Remove key occupation and save it in a variable; print the variable.
person = {
    "name": "Jane",
    "age": 32,
    "occupation": "teacher",
    "hobbies": ["reading", "hiking"],
}
occupation = person.pop("occupation")
print(occupation)

# Try getting value key height (or None, if key does not exist) from the
# dictionary and store it in a variable; print the variable.
height = person.get("height")
print(height, end="\n\n")

# Update the dictionary with the following dictionary:
measurements = {"weight": 75, "height": 1.78, "name": "John"}
person.update(measurements)

# Iterate on the dictionary to print its keys and values.
for key, value in person.items():
    print(f"Key: {key}\nValue: {value}\n")

# Given a list of strings build a dictionary that has each unique string as a
# key and the number of appearances as a value.
#
# E.g. ['hello', 'hello', 'is', 'there', 'anybody', 'in', 'there'] ->
# {'hello': 2, 'is': 1, 'there': 2, 'anybody': 1, 'in': 1}

occurrences = {}
words = ['hello', 'hello', 'is', 'there', 'anybody', 'in', 'there']
for word in words:
    if word not in occurrences:
        occurrences[word] = 1
    else:
        occurrences[word] += 1
print("v1", occurrences)

occurrences = {}
words = ['hello', 'hello', 'is', 'there', 'anybody', 'in', 'there']
for word in words:
    occurrences[word] = occurrences.get(word, 0) + 1
print("v2", occurrences, end="\n\n")
