# Create a list with at least 5 elements.
my_list = [1, 2, 3, 4, 5]
# Print the entire list.
print(my_list)
# Print the reversed list, using slicing.
print(my_list[::-1])
# Print the first element of the list using indexing.
print(my_list[0])
# Print a slice of the list containing elements from index 2 to index 4.
print(my_list[2:4])
# Modify the second element of the list using index assignment.
# Print the modified list.
my_list[1] = 20
print(my_list)
# Modify a slice of the list to replace elements from index 1 to index 3 with
# new values. Print the modified list.
my_list[1:3] = [7, 8, 9]
print(my_list)
# Delete the last element of the list. Print the final modified list.
del my_list[-1]
print(my_list)
