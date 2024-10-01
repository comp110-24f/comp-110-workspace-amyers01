"""Basic syntax of lists"""

# Create an empty list
my_numbers: list[float] = list()  # using a constructor
my_numbers: list[float] = []  # using a literal

my_numbers.append(1.5)

print(my_numbers)

# String Analogy
my_name: str = ""  # literal
my_name: str = str()  # constructor


# Creating an already populated list
game_points: list[int] = [102, 86, 94]
print(game_points)

# Subscription Notation/Indexing
print([102, 86, 94][2])  # option 1
last_game: int = game_points[2]  # option 2
print(last_game)
print(game_points[2])  # option 3

# Modifying by Index
game_points[1] = 72
print(game_points)

# Getting the length
len(game_points)

# Removing an item
game_points.pop(1)
print(game_points)

# function name: display
# parameter : list of integers
# RV: none
# print every element in the input list
# call display on game_points


def display(int_list: list[int]) -> None:
    """Displays all elements of int_list"""

    index: int = 0
    while index < len(int_list):
        print(int_list[index])
        index += 1


display(int_list=game_points)
