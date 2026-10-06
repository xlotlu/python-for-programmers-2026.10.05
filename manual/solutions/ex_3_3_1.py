# Write a program that prints all integers between 500 and 525 (both included)
# using a for loop.
for nr in range(500, 526):
    print(nr, end=" ")

# Write a program that computes the sum of all numbers between 100 and 150
# using a for loop.
number_sum = 0
for nr in range(100, 151):
    number_sum += nr
print("\nThe sum of all numbers between 100 and 150 is", number_sum)

# Write a Python program which iterates the integers from 1 to 50 and prints
# their value. For multiples of three print "Fizz" instead of the number and
# for the multiples of five print "Buzz" instead of the number. For numbers
# which are multiples of both three and five print "FizzBuzz" instead of the
# number.
start = 1
stop = 50

for nr in range(start, stop+1):
    if nr % 3 == 0 and nr % 5 == 0:
        print("FizzBuzz")
    elif nr % 3 == 0:
        print("Fizz")
    elif nr % 5 == 0:
        print("Buzz")
    else:
        print(nr)
