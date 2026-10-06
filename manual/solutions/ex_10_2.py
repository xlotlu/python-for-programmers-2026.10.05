# Write a function convert_temperature(temp, scale) that converts a temperature
# from one scale to another. The function should accept two arguments:
# temp: The temperature value to be converted (a float or an int). scale:
# The scale of the temperature, which can be either "C" for Celsius or "F"
# for Fahrenheit.
#
# The conversion formulas are as follows:
# F = 9 / 5 * C + 32
# C = (F - 32) * 5 / 9
# If the scale provided is neither "C" nor "F", the function should raise a
# ValueError with an appropriate error message.


def convert_temperature(temp, scale):
    if scale.upper() == "F":
        return 9 / 5 * temp + 32
    elif scale.upper() == "C":
        return (temp - 32) * 5 / 9
    else:
        raise ValueError(f"Invalid scale '{scale}' (options are 'F' or 'C').")


if __name__ == "__main__":
    fahrenheit_temp_1 = 68
    celsius_temp_1 = convert_temperature(fahrenheit_temp_1, "c")
    print(f"Temperature is {fahrenheit_temp_1}\xb0F ({celsius_temp_1} \xb0C)")

    celsius_temp_2 = 20
    fahrenheit_temp_2 = convert_temperature(celsius_temp_2, "F")
    print(f"Temperature is {celsius_temp_2}\xb0C ({fahrenheit_temp_2} \xb0F)")

    try:
        convert_temperature(10, "X")
    except ValueError as ex:
        print(ex)
