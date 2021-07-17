# Recursion Exercise 5
# Write a recursive function called get_max that takes a list of numbers as a parameter.
# Return the largest number in the list.
# Expected Output
# If the function call is get_max([1, 2, 3, 4, 5]), then the function would return 5
# If the function call is get_max([11, 22, 3, 41, 15]), then the function would return 41
# Use the max function to return the larger of two numbers.


def get_max(num_list):
    """Recursively returns the largest number from the list"""
    if len(num_list) == 1:
        return num_list[0]
    else:
        return max(num_list[0], get_max(num_list[1:]))


def main():
    print(get_max([1, 2, 3, 4, 5]))
    print(get_max([11, 22, 3, 41, 15]))


if __name__ == "__main__":
    main()
