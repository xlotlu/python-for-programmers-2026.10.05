# Initialize a variable age with the value None. Check if age is None, and,
# if it is, ask the user to input his age. Print the value of variable age.
age = None
# age = 23
if age is None:
    age = int(input("Insert age: "))

# age processing
print(f"In 10 years you will be {age + 10} years old.")
print("Current age:", age)

# In the code above, change age value to a numeric value. Re-run the code.
# What happens?
# The age is not requested from the user
