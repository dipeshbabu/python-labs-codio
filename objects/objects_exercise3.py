"""
Exercise 3
Define the class SuperHero.
The class should have a constructor that accepts the following parameters (in this order):
name- String with the name of the super hero, e.g. "Spider-Man"
secret_identity - String with the true name of the hero, e.g. "Peter Parker"
powers - A list of strings with each element representing a power,
e.g. ["superhuman strength", "superhuman speed", "superhuman reflexes", "superhuman durability",
"healing factor", "spider-sense alert", "heightened senses", "wallcrawling"]
"""


class SuperHero:
    """Define the SuperHero class"""

    def __init__(self, name, secret_indentity, powers) -> None:
        """Initialize the SuperHero class"""
        self.name = name
        self.secret_identity = secret_indentity
        self.powers = powers


hero = SuperHero(
    "Spider-Man",
    "Peter Parker",
    [
        "superhuman strength",
        "superhuman speed",
        "superhuman reflexes",
        "superhuman durability",
        "healing factor",
        "spider-sense alert",
        "heightened senses",
        "wallcrawling",
    ],
)

print(f"Name: {hero.name} \n")
print(f"Secret Identity: {hero.secret_identity} \n")
print(f"Powers: {hero.powers} \n")
