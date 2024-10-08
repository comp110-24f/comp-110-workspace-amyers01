"""Some scope examples"""


def remove_chars(msg: str, char: str) -> str:
    """Returns a copy of msg with all instances of char removed."""
    copy: str = ""  # Set up empty str to copy values over
    index: int = 0  # local variables
    while index < len(msg):
        if msg[index] != char:
            copy = copy + msg[index]  # concadenate, also copy += msg[index]
        index += 1
    return copy


if __name__ == "__main__":
    word: str = "yoyo"  # global variable
    print(remove_chars(word, "y"))
    print(remove_chars(word, "o"))

# only interprets code if directly running file, won't work if importing the file
