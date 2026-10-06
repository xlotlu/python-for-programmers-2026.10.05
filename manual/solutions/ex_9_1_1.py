# Create a dictionary called person that contains the following key-value pairs:
#  "name": "Jane"
#  "age": 32
#  "occupation": "teacher"
#  "hobbies": ["reading", "hiking"]
# print the value for key age
# update the value for key age to 52
# add a new item to the dictionary with key "friends" and value
# ["Anna", "Grace", "Mike"]
# add "cooking" to the hobbies list
# print the dictionary and its length

person = {
 "name": "Jane",
 "age": 32,
 "occupation": "teacher",
 "hobbies": ["reading", "hiking"],
}
print("Person age:", person["age"])
person["age"] = 52
person["friends"] = ["Anna", "Grace", "Mike"]
person["hobbies"].append("cooking")
print("Person dict:", person)
print("Person dict length:", len(person))
