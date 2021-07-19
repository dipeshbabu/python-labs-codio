"""
Exercise 4
Define the class Observation which will help record observational data from a scientific outpost in Antarctica.
The class should have a constructor that accepts parameters for date, temperature, elevation, precipitation, and penguins.
Since Antarctica is a desert, precipitation should default to 0.
date- String with the date of the observation, e.g. "October 26, 2019"
temperature - Float with the temperature in Celsius, e.g. -47
elevation - Float with elevation in meters, e.g. 329.4
penguins - Integer representing the number of penguins observed, e.g. 3
precipitation- Float with precipitation in centimeters, e.g. 0.7
"""


class Observation:
    """Define the observation class"""

    def __init__(self, date, temperature, elevation, penguins, precipitation=0):
        self.date = date
        self.temperature = temperature
        self.elevation = elevation
        self.penguins = penguins
        self.precipitation = precipitation


observation1 = Observation("October 26, 2019", -47, 329.4, 3, 0.7)

print(f"Date: {observation1.date} \n")
print(f"Temperature: {observation1.temperature} \n")
print(f"Elevation: {observation1.elevation} \n")
print(f"Penguins: {observation1.penguins} \n")
print(f"Precipitation: {observation1.precipitation} \n")
