# Write a function that takes a number as a parameter and prints its square.
def print_square(x):
    print(x ** 2)


# Write another function that takes a number as a parameter and returns the
# square.
def return_square(x):
    return x ** 2


# Are the results of the two functions above different? Which of the two
# functions can be used to compute x2 + y2 ?
print("Results are equal:", print_square(2) == return_square(2))
square_sum = return_square(2) + return_square(3)
print(square_sum)


# Write a function get_rectangle_properties that takes the width and height of a
# rectangle as parameters and returns the area and perimeter of the rectangle.
# Call the function and assign the result to two variables.
def get_rectangle_properties(width, height):
    return width * height, 2 * (width + height)


area, perimeter = get_rectangle_properties(20, 30)
print("Area is", area, "and perimeter is", perimeter)


# Write a function build_html which receives two parameters tag and content, and
# returns the following string:
# <tag>content</tag>
#
# Call it so that you build the following output:
# <div><h1>Functions</h1><p>Functions are fun!</p></div>
def build_html(tag, content):
    return f"<{tag}>{content}</{tag}>"


header = build_html("h1", "Functions")
paragraph = build_html("p", "Functions are fun!")
div = build_html("div", header + paragraph)
print(div)
