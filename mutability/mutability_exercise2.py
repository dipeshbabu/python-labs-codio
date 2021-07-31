"""
Exercise 2
Using the same CelestialBody class, write a static method closer_to_sun that compares
two CelectialBody objects and returns the name of the object that is closes to the sun.
Expected Output
If the objects mercury and venus are compared, then the method would return Mercury.
"""


class CelestialBody:
    """Represents a celestial body"""

    def __init__(self, name, diameter, distance, moons):
        self.name = name
        self.diameter = diameter
        self.distance = distance
        self.moons = moons

    @staticmethod
    def closer_to_sun(body1, body2):
        """
        Returns the name of the body
        that is closest to the sun
        """
        if body1.distance < body2.distance:
            return body1.name
        else:
            return body2.name


mercury = CelestialBody("Mercury", 4879.4, 57909000, 0)
venus = CelestialBody("Venus", 12103.6, 108160000, 0)
