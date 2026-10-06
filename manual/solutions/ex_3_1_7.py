# Create a Python program that calculates the delivery fee for an online order
# based on the distance of the delivery and the weight of the package. The
# pricing rules are as follows:
#
#  For distances under 10 km:
#   Packages weighing less than 5 kg: $5 delivery fee.
#   Packages weighing 5 kg or more: $8 delivery fee.
#  For distances of 10 km or more:
#   Packages weighing less than 5 kg: $10 delivery fee.
#   Packages weighing 5 kg or more: $15 delivery fee.
# Prompt the user to enter the distance and the weight of the package and
# output the delivery fee.
distance = int(input("Enter distance: "))
weight = int(input("Enter package weight: "))

if distance < 10:
    if weight < 5:
        delivery_fee = 5
    else:
        delivery_fee = 8
else:
    if weight < 5:
        delivery_fee = 10
    else:
        delivery_fee = 15
print(f"Delivery fee is {delivery_fee}$.")

# Write a Python program for checking the speed of drivers.
#   - If speed is less than or equal to 50, it should print "OK".
#   - Otherwise, for every 5 km above the speed limit (50), it should give the
# driver one demerit point and print the total number of demerit points.
# For example, if the speed is 60, it should print: "Points: 2".
#   - If the driver gets more than 12 points, display "License suspended"
# instead of the number of demerit points.
# Prompt the user to enter the speed and output the appropriate message.

MAX_SPEED = 50  # constants are usually uppercase
speed = int("Enter speed: ")

if speed <= MAX_SPEED:
    print("OK")
else:
    demerit_points = (speed - MAX_SPEED) // 5
    if demerit_points <= 12:
        print("Points:", demerit_points)
    else:
        print("License suspended")
