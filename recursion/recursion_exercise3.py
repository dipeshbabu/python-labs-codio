# Recursion Exercise 3
# Write a recursive function called bunny_ears that takes the number of bunnies (an integer) as a parameter.
# Return the number of bunny ears (2 per bunny). Do not use multiplication; instead use addition.
# Expected Output
# If the function call is bunny_ears(8), then the function would return 16
# If the function call is bunny_ears(0), then the function would return 0


def bunny_ears(bunnies):
    """Recursively determines the number of bunny ears (2 per bunny)"""
    return bunny_ears(bunnies - 1) + 2 if bunnies > 0 else 0


if __name__ == "__main__":
    print(bunny_ears(8))
    print(bunny_ears(0))
