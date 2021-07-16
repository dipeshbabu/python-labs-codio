####################################################################################################################
#                                 Functions - Lab Exercise 1
#
# Write a function called avg that takes two parameters. Return the average of these two parameters.
# If the parameters are not numbers, return the string, Please use two numbers as parameters.
#
#  Expected Output
#  If the function call is avg(10,25), then the function would return 17.5
#  If the function call is avg(10, "cat"), then the function would return Please use two numbers as parameters
#
####################################################################################################################

# If the function call is avg(10, 25):
def avg(num1, num2):
    """Return the average of the two numbers"""
    if type(num1) == type("Hello") or type(num2) == type("Hello"):
        return "Please use two numbers as parameters"
    return (num1 + num2) / 2


if __name__ == "__main__":
    print(avg(10, 25))
    print(avg(10, "cat"))
