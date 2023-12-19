import numpy as np

def celsius_to_fahrenheit(celsius_array):
    # Convert Centigrade to Fahrenheit using the formula
    fahrenheit_array = (celsius_array * 9/5) + 32
    return fahrenheit_array

# Example: Convert a list of Centigrade temperatures to Fahrenheit
celsius_temperatures = np.array([0, 10, 20, 30, 40])
fahrenheit_temperatures = celsius_to_fahrenheit(celsius_temperatures)

# Display the results
print("Centigrade Temperatures:", celsius_temperatures)
print("Fahrenheit Temperatures:", fahrenheit_temperatures)
