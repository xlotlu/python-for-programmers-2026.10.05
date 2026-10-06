# Declare a variable called my_age and assign it your current age as an integer.
# Declare a variable called friend_age and assign it the age of a friend as an
# integer. Calculate the age difference between you and your friend and store
# it in a variable called age_difference. Print the age difference.
my_age = 35
friend_age = 41
age_difference = my_age - friend_age
print(age_difference)

# Romania's GDP in 2022 was 284 billion euros. In the same year, Romania's
# population was 19.5 million. Define two variables gdp and population and
# store these values. Compute and display Romania's GPD per capita in 2022.
gdp = 284e9
population = 19.5e6
gdp_per_capita = gdp / population
print(gdp_per_capita)

# Declare a variable called celsius_temp and assign it a temperature in Celsius
# as a float. Convert the temperature to Fahrenheit using the formula:
# Fahrenheit = (Celsius * 9/5) + 32. Store the result in a variable called
# fahrenheit_temp. Print the Fahrenheit temperature.
celsius_temp = 16
fahrenheit_temp = (celsius_temp * 9/5) + 32
print(fahrenheit_temp)

# Declare a variable called distance_meters and assign it a length in meters as
# a float. Convert the length to feet using the conversion factor:
# 1 meter = 3.28084 feet. Store the result in a variable called distance_feet.
# Print the distance in feet.
distance_meters = 200
distance_feet = distance_meters * 3.28084
print(distance_feet)

# Define a variable called total_minutes and assign it a random value chosen by
# you between 0 and 1440. Consider this to be the number of minutes passed after
# midnight. What time would a digital 24h clock show? Compute and display the
# two values: hour and minute.
total_minutes = 832
hour = total_minutes // 60
minute = total_minutes % 60
print(hour, minute)
