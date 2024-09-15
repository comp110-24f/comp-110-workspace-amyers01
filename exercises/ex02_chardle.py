"""EX02 - Chardle - A cute step toward Wordle."""

__author__ = "730654167"


def input_word() -> str:
    """Display Word instructions"""
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit()


# determines the length of the word and prints if correct


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit()


# determines if letter inputted is one or more


def contains_char(word: str, letter: str) -> None:
    input("Searching for " + letter + " in " + word)
    index: int = 0
    count: int = 0
    while index < len(word):
        if word[index] == letter:
            print(letter + " found at index " + str(index))
            count = count + 1
        index = index + 1

    if count > 1:
        print(str(count) + " instances of " + letter + " in " + word)
    elif count == 1:
        print(str(count) + " instance of " + letter + " in " + word)
    else:
        print("No instances of " + letter + " in " + word)


# Use a while loop to determine if word and letter match
# have to create a new variable index to get each index of the word
# add in the count and print statement IF the letter and index match
# change index no matter what = after the if statement


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
