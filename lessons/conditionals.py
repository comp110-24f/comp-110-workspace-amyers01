"""Practice with Conditionals"""


def less_than_10(num: int) -> None:
    """Tell me if num is < 10 (less than 10)"""
    dub: int = num * 2
    dub = dub - 1
    print(dub)
    if num < 10:
        print("Small number!")  # alternate: return True
    else:
        print("Big number!")  # alternate: return False
    print("Have a nice day!")
    # interpret this line of code either way


less_than_10(num=5)


def should_i_eat(hungry: bool) -> None:
    """Tells me whether or not to eat based on hunger."""
    if hungry:  # can be "if hunger is True:" conditional/boolean expression
        print("Eat some food")  # "then" block
    else:
        print("Do your Comp 110 homework instead")  # "else" block
    print("I'm proud of you <3")  # etiher way, be kind to yourself


should_i_eat(hungry=True)


def check_first_letter(word: str, letter: str) -> str:
    """Check if letter is first character of word"""
    if word[0] == letter:
        return "match!"
    else:
        return "no match!"


# print(check_first_letter(word="happy", letter="h"))
# print(check_first_letter(word="happy", letter="s"))
