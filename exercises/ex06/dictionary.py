"""Exercise 06 - Practice with Dictionary Functions."""

__author__ = "730654167"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Creates a dictionary inverting the keys and value of input dictionary"""
    d_invert: dict[str, str] = {}
    for key in d:
        if d[key] in d_invert:
            raise KeyError("There are dupliicate keys in d_invert!")
        d_invert[d[key]] = key
    return d_invert


# loops through the keys in inputed dict
# calls the key of input dict and takes the value as the key of new dict
# takes the key called and makes it the value of the new dict


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


# creates a new dictionary (count) and new string for most popular color
# loops through the names in the input dictionary
# creates a new variable color for each value (color) in the input dict
# if the color is already in the count dict, it adds one to the value (count)
# if the color is not in count dict, it assigns the value to 1
# creates a new variable (max_num) for the max number of a color
# loops through the count dict keys and if the value is greater than max_num = max_num
# the corresponding color is the popular_color
# if there is a tie, two colors have the same value and are max, returns first in dict


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
