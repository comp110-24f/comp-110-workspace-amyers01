"""Practice with functions."""

from random import randint

print(randint(3, 17))


# Function Definition
def sum(num1: int, num2: int) -> int:
    """Return the sum of num1 and num2."""
    # Adding the colon int tells that its an integer, without this it would error.
    # Have to put the colon after the return type, otherwise = error.
    return num1 + num2


# Function Call
print(sum(num1=2, num2=13))  # <- these are arguments
# Always remember to add print
