def get_first(input: list[str]) -> str:
    """Return first element."""
    if len(input) == 0:
        return ""
    return input[0]


def remove_first(input: list[str]) -> None:
    """Remove first element from input."""
    input.pop(0)


def get_and_remove_first(input: list[str]) -> str:
    """Remove AND return first element"""
    first_element: str = input[0]
    input.pop(0)
    return first_element


get_and_remove_first(["dog", "cat", "bird"])
