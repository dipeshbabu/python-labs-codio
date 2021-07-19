"""
Exercise 5
Define the class BigCat which will help record information on the animals in the Panthera genus
(tiger, lion, jaguar, leopard, and snow leopard).
Since all animals are in the same genus, the object should have the class attribute genus with the value panthera.
The constructor should accept the following parameters (in this order):
species- String with the species of the animal, e.g. "tigris"
common_name - String with the common name of the animal, e.g. "tiger"
habitat - List of strings with location of the animal, e.g. ["asia"]
"""


class BigCat:
    """Define the BigCat class"""

    genus = "panthera"

    def __init__(self, species, common_name, habitat):
        """Initialize the BigCat"""
        self.species = species
        self.common_name = common_name
        self.habitat = habitat


observation1 = BigCat("tigris", "tiger", ["asia"])

print(f"Species: {observation1.species} \n")
print(f"Common Name: {observation1.common_name} \n")
print(f"Habitat: {observation1.habitat} \n")
