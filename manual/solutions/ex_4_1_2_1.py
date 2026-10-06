# Given the following list:
greetings = ["hello", "hi", "good morning", "good afternoon"]
# check, for each of the following objects, if they are in the list:
# "hi", "good", ["hello", "hi"]
print("hi" in greetings)
print("good" in greetings)
print(["hello", "hi"] in greetings)

# Add "good evening" and "hey there" (using in place list concatenation) to
# greetings and print the new value of the list.
greetings += ["good evening", "hey there"]
print(greetings)

# Create a list with elements from range(562, 873, 17). Is 800 in this list?
numbers = list(range(562, 873, 17))
print(800 in numbers)

# Multiply the list above by 3 and assign the result to a new variable.
# Print the new list.
more_numbers = numbers * 3
print(more_numbers)
