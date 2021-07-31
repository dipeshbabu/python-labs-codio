"""
Exercise 1
The code below creates the CelestialBody class as well as the function compared_to_earth.
Transform the compared_to_earth function so that it becomes an instance method of the CelestialBody class.
Expected Output
Printing the compared_to_earth instance method should return 11.208892860782516.
"""


class CelestialBody:
    """Represents a celestial body"""

    def __init__(self, name, diameter, distance, moons):
        self.name = name
        self.diameter = diameter
        self.distance = distance
        self.moons = moons

    def compared_to_earth(self):
        """
        Determines the size of a celestial
        body relative to Earth using diameter
        """
        earth = 12756.3
        relative_size = self.diameter / earth
        return relative_size


planet = CelestialBody("Jupiter", 142984, 778360000, 79)
print(planet.compared_to_earth())
