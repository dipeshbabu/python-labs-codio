####################################################################################################################
#                                     Functions - Lab Exercise 2
#
# Write a function called odds_or_evens that takes a boolean and a list of integers as parameters.
# If the boolean parameter is True, return a list of only even numbers.
# If the boolean parameter isFalse, return a list of only odd numbers.
#
#  Expected Output:
#  If the function call is odds_or_evens(True, [8, 13, 22, 31]), the the function would return [22, 8]
#  If the function call is odds_or_evens(False, [8, 13, 22, 31]), the the function would return [13, 31]
#
####################################################################################################################

# 1st method
def odds_or_evens(boolean, my_list):
    if boolean:
        for i in my_list:
            if i % 2 != 0:
                my_list.remove(i)
    else:
        for i in my_list:
            if i % 2 == 0:
                my_list.remove(i)

    return my_list


# 2nd method
def odds_or_evens(my_bool, nums):
    """Returns all of the odd or
    even numbers from a list"""
    return_list = []
    for num in nums:
        if my_bool:
            if num % 2 == 0:
                return_list.append(num)
        else:
            if num % 2 != 0:
                return_list.append(num)

    return return_list


if __name__ == "__main__":
    print(odds_or_evens(True, [8, 13, 22, 31]))
    print(odds_or_evens(False, [8, 13, 22, 31]))
