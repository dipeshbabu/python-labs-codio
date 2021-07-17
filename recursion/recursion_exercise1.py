# Recursion Exercise 1
# Write a recursive function called recursive_sum that takes an integer as a parameter.
# Return the sum of all integers between 0 and the number passed to recursive_sum.
# Expected Output
# If the function call is recursive_sum(5), then the function would return 15
# If the function call is recursive_sum(10), then the function would return 55


# 1st solution
def recursive_sum(num):
    return num + recursive_sum(num - 1) if num > 0 else 0


# 2nd solution
def recursive_sum(num):
    if num == 0:
        return 0
    else:
        return num + recursive_sum(num - 1)


if __name__ == "__main__":
    print(recursive_sum(5))
    print(recursive_sum(10))
