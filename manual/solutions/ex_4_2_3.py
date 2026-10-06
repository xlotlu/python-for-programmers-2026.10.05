# Given the following variables:

x = 10
first_tuple = x + 2, x + 1, x
second_tuple = tuple(range(5))
third_tuple = (2, 3, 4)

# create a new tuple final_tuple containing:
# - all elements in first_tuple, two times
# - elements from index 1 (inclusive) up to index 4 (exclusive) from
# second_tuple
# - element on index 1 from third_tuple

# Do not hardcode values, the code should still work if we change the initial
# tuples. Use tuple concatenation, multiplication, indexing and slicing.
final_tuple = first_tuple * 2 + second_tuple[1:4] + (third_tuple[1], )
print(final_tuple)

# Given the following tuple:

movies = (
    ("Titanic", 7.9),
    ("Star Wars", 8.6),
    ("The Lord of the Rings", 9),
    ("Harry Potter", 7.6),
    ("Transformers", 7),
)
# representing movie titles and ratings:
#
# iterate on it, printing the names of the movies with a rating higher than 8
# (consider these to be recommended movies);
recommended_count = 0
for movie, rating in movies:
    if rating > 8:
        recommended_count += 1
        print(movie)

# write a message saying "I have recommended x ouf of y movies", where x and y
# should be the actual counts of recommended and total movies.
print(f"I have recommended {recommended_count} out of {len(movies)} movies.")
