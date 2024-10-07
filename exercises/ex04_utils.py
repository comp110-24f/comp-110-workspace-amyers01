"""Exercise 04 - List Utility Functions"""

__author__ = "730654167"


def all(input: list[int], num: int) -> bool:
    """Returns True is the number and all values in list match"""
    idx: int = 0
    match: bool = False
    while idx < len(input):
        if input[idx] == num:
            match = True
        else:
            match = False
        idx += 1
    return match


# enter a list and a number
# goes through each index of list to see if matches the number


def max(input: list[int]) -> int:
    """Returns the max number in the list"""
    if len(input) == 0:
        raise ValueError("max() arg is an empty List")
    idx: int = 0
    value: int = input[0]
    while idx < len(input):
        if input[idx] > value:
            value = input[idx]
        idx += 1
    return value


# value is set to input at index 0
# loops through each index of list to see if it is bigger than value
# if it is bigger, that number is now set to be value


def is_equal(list_1: list[int], list_2: list[int]) -> bool:
    """Checks if every element in both lists are equal"""
    idx: int = 0
    if len(list_1) != len(list_2):
        return False
    while idx < len(list_1) and idx < len(list_2):
        if list_1[idx] == list_2[idx]:
            idx += 1
        else:
            return False
    return True


# Don't assume length of lists are equal so we have to check
# if lists are not equal - returns False and ends function
# iterates through each element of each list, checking if they match
# if they match match continues through loop till end and returns True
# if they don't match returns False and ends the function


def extend(list_1: list[int], list_2: list[int]) -> None:
    """Appending list_2 to list_1"""
    list_2_idx: int = 0
    while list_2_idx < len(list_2):
        list_1.append(list_2[list_2_idx])
        list_2_idx += 1


# adds the values of list 2 to the end of list 1
# increasing the index
