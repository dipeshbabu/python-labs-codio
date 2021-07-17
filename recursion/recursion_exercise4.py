# Recursion Exercise 4
# Write a recursive function called reverse_string that takes a string as a parameter.
# Return the string in reverse order. Hint, the slice operator will be helpful when solving this problem.
# Expected Output
# If the function call is reverse_string("cat"), then the function would return tac
# If the function call is reverse_string("house"), then the function would return esuoh
# Hint
# The recursive pattern is to take the last character from the string and pass the string
# (minus the last character) to the function.


# 1st solution
def reverse_string(string):
    """Recursively returns the string in reverse order"""
    if len(string) == 1:
        return string
    else:
        return reverse_string(string[1:]) + string[0]


# 2nd solution
def reverse_string(string):
    if len(string) == 1:
        return string[0]
    else:
        return string[-1] + reverse_string(string[:-1])


if __name__ == "__main__":
    print(reverse_string("cat"))
    print(reverse_string("house"))
