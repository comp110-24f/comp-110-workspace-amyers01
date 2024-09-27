"""Exercise 03 - Final Step of Wordle."""

__author__ = "730654167"


def input_guess(secret_word_len: int) -> str:
    """Returns the word guessed of the correct length"""
    guess: str = input(f"Enter a {secret_word_len} character word: ")
    while len(guess) != secret_word_len:
        # if len(guess) == secret_word_len:
        # return guess
        # else:
        guess = input(f"That wasn't {secret_word_len} chars! Try again: ")
    return guess


def contains_char(secret: str, letter: str) -> bool:
    """Returns True or False if the letter is contained in the word"""
    assert len(letter) == 1
    index: int = 0
    while index < len(secret):
        if secret[index] == letter:
            return True
        index += 1
    return False


# changes the value for match from True or False depending on if the letter is in word
# Iteriates through each index, if match then returns True
# If completes the while loop with no match, returns False


def emojified(guess: str, secret: str) -> str:
    """Compares the guess and word with colored boxes"""
    assert len(guess) == len(secret)
    index: int = 0
    box: str = ""
    WHITE_BOX: str = "\U00002B1C"
    GREEN_BOX: str = "\U0001F7E9"
    YELLOW_BOX: str = "\U0001F7E8"
    while index < len(guess):
        if guess[index] == secret[index]:
            box += GREEN_BOX
        elif contains_char(secret, guess[index]):
            box += YELLOW_BOX
        else:
            box += WHITE_BOX
        index += 1
    return box


# Iteriates through each index of guess and secret to see if they match
# If they do, adds a green box to "box" string
# Elif - calls contains_char and that index of guess is the letter, and secret is word
# If the indexed letter is contained in "secret" = adds a yellow box to "box" string
# Else - if indexed letter isn't contained in secret, it adds white box to "box" string


def main(secret: str) -> None:
    """The entrypoint of the program and main game loop."""
    secret_word_len: int = len(secret)
    turn: int = 1
    won: bool = False
    while turn <= 6 and not won:
        print(f"=== Turn {turn}/6 ===")
        guess = input_guess(secret_word_len)
        print(emojified(guess, secret))
        if guess == secret:
            print(f"You won in {turn}/6 turns!")
            won = True
        else:
            turn += 1
            print(emojified(guess, secret))

        if turn > 6:
            print("X/6 - Sorry, try again tomorrow!")

    # Have to define secret_word_len as a local variable
    # call input_guess and set secret_word_len as parameter
    # Add local variable turns for while loop condition
    # add local variable guess under the turn number
    # calls emojified function with guess and secret


if __name__ == "__main__":
    main(secret="codes")
