# Recursion Exercise 2
# Write a recursive function called list_sum that takes a list of numbers as a parameter.
# Return the sum of all of the numbers in the list.
# Hint, the slice operator will be helpful in solving this problem.
# Expected Output
# If the function call is list_sum([1, 2, 3, 4, 5]), then the function would return 15
# If the function call is list_sum([10, 12.5, 10, 7]), then the function would return 39.5


def list_sum(num_list):
    """Returns the sum of all of the numbers in the list"""
    if len(num_list) == 1:
        return num_list[0]
    else:
        return num_list[0] + list_sum(num_list[1:])


if __name__ == "__main__":
    print(list_sum([1, 2, 3, 4, 5]))
    print(list_sum([10, 12.5, 10, 7]))
