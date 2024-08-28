"""Planning a Tea Party Exercise 1!"""

__author__ = "730654167"


def main_planner(guests: int) -> None:
    """Details for planning a tea party"""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(guests)))
    print("Treats: " + str(treats(guests)))
    print("Cost: $" + str(cost(tea_bags(guests), treats(guests))))

    # Taking the number of guests and using each individual function to make a
    # string and print on TH
    # Have to make the integers strings for them to print


def tea_bags(people: int) -> int:
    """Calculates the number tea bags based on the number of guests attending"""
    return people * 2

    # Defined the function named tea_bags and 2 tea bags per person


def treats(people: int) -> int:
    """Calculates the number of treats for each person based on the number of drinks"""
    # Defined the function named treats
    return int(tea_bags(people=people) * 1.5)

    # When calling the function, have to call tea_bags with the people
    # integer then multiply by 1.5 for treats
    # Use people = people for tea_bags people and treats people
    # After muliplying it by 1.5, have to add int around because would be a float
    # The solution would be saying the number of people get
    # 2 tea_bags = 2 drinks * 1.5 treats
    # ex. 3 * 2 * 1.5 = 9


def cost(tea_count: int, treat_count: int) -> float:
    """Computes the cost of tea bags and treats combined"""
    return tea_count * 0.50 + treat_count * 0.75

    # Calculates the number of total tea bags,
    # Do NOT need to know the number of people, just the total number of tea bags/treats


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
