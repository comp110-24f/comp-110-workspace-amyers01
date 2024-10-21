"""Exercise 5 - Implementing list utility functions"""

__author__ = "730654167"


def only_evens(input: list[int]) -> list[int]:
    """Creates a new list containing only the even elements of the input list"""
    even: list[int] = []
    for num in input:
        if num % 2 == 0:
            even.append(num)
        num += 1
    return even


# even is an empty list, taking on the elements that are even from input


def sub(input: list[int], start: int, end: int) -> list[int]:
    """Creates a subset list of the input list between start and end indexes"""
    if start < 0:
        start = 0
    if end > len(input):
        end = len(input)
    if len(input) == 0 or start >= len(input) or end <= 0:
        return []
    return input[start:end]


# takes the value of the list with start index and value of the list with the end index
# makes a subset list of those variables, plus the varaibles between
# ([start:end]) == start index to end index (not including)


def add_at_index(input: list[int], elem: int, idx: int) -> None:
    """Modifies the input list to place the element at the given index"""
    if idx < 0 or idx > len(input):
        raise IndexError("Index is out of bounds for the input list")
    input.append(elem)
    for insert in range(len(input) - 1, idx, -1):
        input[insert] = input[insert - 1]
    input[idx] = elem


# if the index argument is less than 0 or greater than the length = error
# add elem to the end of the list
# iterates over each element in the list, starting from the end of the list
# start: len(input) -1 = length of list is 5, then the last index value is 4
# end: at the index value argument
# step to each "insert" value by -1 = going backwards by 1, since starting at end
# input[insert] value becomes input[insert-1] - value to left
# if 0 is at input[3], and 4 is to the left at input[2], assign 4 to input[3] = input[3-1]
# once get to the index argument value, assign that input[idx] = elem
