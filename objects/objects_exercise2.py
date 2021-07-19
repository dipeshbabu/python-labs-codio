"""
Exercise 2
Define the class Cat.
The class should have a constructor but without any parameters.
The constructor will generate the following attributes.
breed - "american shorthair"
color - "black"
name - "kiwi"
Test your code with print statements and the TRY IT button below before submitting your work.
"""


class Cat:
    """Define the cat class"""

    def __init__(self):
        """Initialize the cat"""
        self.breed = "american shorthair"
        self.color = "black"
        self.name = "kiwi"


cat1 = Cat()

print(f"Breed: {cat1.breed} \n")
print(f"Color: {cat1.color} \n")
print(f"Name: {cat1.name} \n")
