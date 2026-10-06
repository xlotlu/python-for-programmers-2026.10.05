# Given the following variables:
name = "Jane"
age = 20
is_student = True
# create a person tuple with their values. Print the tuple and its type.
person = (name, age, is_student)
print(person, type(person), end="\n\n")

# Given the following data structure:
friends = [
    ("Jane", 20, ["reading", "hiking", "biking"]),
    ("Mike", 17, ["hiking", "fishing"]),
    ("Anna", 25, []),
    ("Sam", 40, ["playing guitar"]),
    ("Dan", 34, ["painting", "reading"]),
 ]
# containing name, age and hobbies:
# first, iterate on friends list, print every item and its type;
for friend in friends:
    print(friend, type(friend))
print()

# then, iterate on friends list using tuple unpacking for higher readability,
# and print each item in the tuples and their respective types;
for name, age, hobbies in friends:
    print(name, type(name))
    print(age, type(age))
    print(hobbies, type(hobbies))
print()

# iterate a third time on friends list, use tuple unpacking, and print the names
# of people who are over 18 and have at least two hobbies.
for name, age, hobbies in friends:
    if age > 18 and len(hobbies) >= 2:
        print(name)
