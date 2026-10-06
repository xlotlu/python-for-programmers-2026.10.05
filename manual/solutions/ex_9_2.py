# Create a set called visited_cities that contains the names of five cities you
# have visited in the past. Create a second set called bucket_list that contains
# the names of three cities you absolutely want to visit.
#
# Create the set bucket_list_completed which contains cities that are in both
# visited_cities and bucket_list (intersection).
# Create the set all_cities which contains cities that are in either
# visited_cities or bucket_list (union).
# Create the set must_visit which contains cities that are in bucket_list,
# but not in visited_cities (difference).

visited_cities = {"Paris", "London", "Lisbon", "Munich", "Zurich"}
bucket_list = {"Tokyo", "Paris", "Zurich", "New York"}
bucket_list_completed = visited_cities & bucket_list
all_cities = visited_cities | bucket_list
must_visit = bucket_list - visited_cities
print("Bucket list completed:", bucket_list_completed)
print("All cities:", all_cities)
print("Must visit:", must_visit, end="\n\n")


# Write a Python program that counts the number of distinct words from a string.
# A word=a sequence of characters that is not whitespace (space, newline, tab).

# E.g.

my_str = """beautiful is better than ugly
explicit is better than implicit
simple is better than complex
complex is better than complicated
flat is better than nested
sparse is better than dense"""
# Should print: 14 distinct words

all_words = my_str.split()
print("All words:", all_words)

unique_words = set(all_words)
print("Unique words:", unique_words)

print(f"{len(unique_words)} distinct words.")
