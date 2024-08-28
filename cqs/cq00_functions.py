"""My first CQ in COMP 110!"""

__author__ = "730654167"


def mimic(message: str) -> str:
    """Returning the string message back"""
    return message


def main() -> None:
    """Prints the message"""
    print(mimic(message=input("What is your message?")))


if __name__ == "__main__":
    main()
