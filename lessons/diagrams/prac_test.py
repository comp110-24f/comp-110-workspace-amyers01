from lessons.diagrams.prac import reverse_multiply


def test_reverse_multiply() -> None:
    a: list[int] = [2, 4, 6, 8]
    assert reverse_multiply(a) == [16, 12, 8, 4]
