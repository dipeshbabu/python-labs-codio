"""
Exercise 3
Using the same CelestialBody class, create a factory method called make_earth.
This method returns a CelestialBody object for planet Earth. Earth is 149,600,000 km
from the Sun, has a diameter of 12,756.3 km, and has one moon.
Expected Output
The factory method should return a CelestialBody object.
This object should be able to do the following things:
print(my_planet.name) will return Earth
print(my_planet.distance) will return 149600000
print(my_planet.diameter) will return 12756.3
print(my_planet.moons) will return 1
"""


class CelestialBody:
    """Represents a celestial body"""

    def __init__(self, name, diameter, distance, moons):
        self.name = name
        self.diameter = diameter
        self.distance = distance
        self.moons = moons

    @classmethod
    def make_earth(cls):
        return CelestialBody("Earth", 12756.3, 149600000, 1)


my_planet = CelestialBody.make_earth()
print(my_planet.name)
print(my_planet.diameter)
print(my_planet.distance)
print(my_planet.moons)
