"""Exercise 06 - Practice with Dictionary Functions."""

__author__ = "730654167"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Creates a dictionary inverting the keys and value of input dictionary"""
    d_invert: dict[str, str] = {}
    for key in d:
        new_key: str = d[key]
        new_value: str = key
        d_invert[new_key] = new_value
        if new_key in d_invert:
            raise KeyError("There are dupliicate keys in d_invert!")
    return d_invert


# takes the key of the input dict and places it as the value of inverted dict.
# takes the value of input dict and places it as the value of inverted dict.


def favorite_color(d: dict[str, str]) -> str:
    count: dict[str, int] = {}
    popular_color: str = ""
    for name in d:
        color: str = d[name]
        if color not in count:
            count[color] = 1
        else:
            count[color] += 1
    max_num: int = 0

    for color in count:
        if count[color] > max_num:
            max_num = count[color]
            popular_color = color
        elif count[color] == max_num and popular_color != color:
            return popular_color
        return popular_color


print(favorite_color({"a": "green", "b": "blue"}))


# WORK ON FAVORITE COLORS


def count(d: list[str]) -> dict[str, int]:
    """Creates a dict for each element in list and the number of times it appears"""
    new_d: dict[str, int] = {}
    for elem in d:
        if elem in new_d:
            new_d[elem] += 1
        else:
            new_d[elem] = 1
    return new_d


# creates an empty list called new_d
# iterates through each element in the list
# if the element is in the dictionary, it increases the count (value) by 1
# otherwise, it will add the value, equal to 1


def alphabetizer(words: list[str]) -> dict[str, list[str]]:
    """Creates a dict with key of first letter of words and value a list of words
    begininning with that letter"""
    sort: dict[str, list[str]] = {}
    for word in words:
        letter = word[0].lower()
        if letter not in sort:
            sort[letter] = []
        sort[letter].append(word)
    return sort


# initalize an empty string for the sorted words.
# iterate through each element in the list.
# the letter is the 0th index (first letter) and takes it as automatical lowercase.
# if the letter is not in the sorted dictionary - it creates an empty list.
# if the letter is in the dictionary and after adding a new list
# append the word to the corresponding letter.


def update_attendance(log: dict[str, list[str]], day: str, student: str) -> None:
    """Adds students who were present for the day to the attendence dictionary"""
    if day not in log:
        log[day] = []
    if student not in log[day]:
        log[day].append(student)


# mutates the inputted dictionary
# if the day is not in the attendance log, it adds it and sets value to an empty list
# then it looks at the students
# if the student is not in the log for that day, it appends it to the list (values)
