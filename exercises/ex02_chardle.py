"""EX02 -Chardle - A cute step toward Wordle."""

__author__ = "730654167"


def input_word() -> str:
    """Display Word instructions"""
    word: str = input("Enter a 5-character word: ")
    if len(word) == 5:
        return word
    else:
        print("Error: Word must contain 5 characters.")
        exit(input_word())


# determines the length of the word and prints if correct


def input_letter() -> str:
    letter: str = input("Enter a single character: ")
    if len(letter) == 1:
        return letter
    else:
        print("Error: Character must be a single character.")
        exit(input_letter())


# determines if letter inputted is one or more


def contains_char(word: str, letter: str) -> None:
    input("Searching for " + letter + " in " + word)
    count: int = 0
    if word[0] == letter:
        print(letter + " found at index 0")
        count = count + 1

    if word[1] == letter:
        print(letter + " found at index 1")
        count = count + 1

    if word[2] == letter:
        print(letter + " found at index 2")
        count = count + 1

    if word[3] == letter:
        print(letter + " found at index 3")
        count = count + 1

    if word[4] == letter:
        print(letter + " found at index 4")
        count = count + 1

    if not (letter in word):
        print(letter + " not found in " + word)
        count = 0

    if count > 0:
        print(str(count) + " instances of " + letter + " found in " + word)
    else:
        print("No instances of " + letter + " found in " + word)


# if functions determine if letter and index match
# not using else because we need to see if all indexes match
# if not(letter in word) outputs printed text if the letter is not in the word
# count = counts the number of times a letter is in the word then prints if/else
# make count a string so it prints correctly
# count is greater than 0, prints message, count is less than 0, prints else message


def main() -> None:
    contains_char(word=input_word(), letter=input_letter())


if __name__ == "__main__":
    main()
