"""Exercise 5 - defining unit tests for utility functions"""

__author__ = "730654167"

from exercises.ex05.utils import only_evens, sub, add_at_index


def test_return_only_evens() -> None:
    """Ensures that only_evens returns the expected value"""
    a: list[int] = [1, 2, 3, 4]
    assert only_evens(a) == [2, 4]


def test_process_only_evens() -> None:
    """Ensures that only_evens does not mutate, but has desired effect"""
    a: list[int] = [1, 2, 3, 4]
    even: list[int] = only_evens(a)
    assert even == [2, 4]


def test_edge_only_evens() -> None:
    """Ensures correct value is returned on a list with no evens"""
    a: list[int] = [7, 11, 5]
    assert only_evens(a) == []


def test_return_sub() -> None:
    """Ensures that sub returns the expected value"""
    a: list[int] = [23, 24, 37, 44]
    first: int = 1
    last: int = 3
    assert sub(a, first, last) == [24, 37]


def test_process_sub() -> None:
    """Ensures that sub does not mutate, but has desired effect"""
    a: list[int] = [23, 24, 37, 44]
    first: int = 1
    last: int = 3
    sub(a, first, last)
    assert a[first:last] == [24, 37]


def test_edge_sub() -> None:
    """Ensures correct value is returned on an unconvential list, start, or end"""
    a: list[int] = []
    first: int = 7
    last: int = 2
    sub(a, first, last)
    assert sub(a, first, last) == []


def test_return_add_idx() -> None:
    """Ensures that add_at_index returns the expected value"""
    a: list[int] = [7, 9, 10, 15]
    num: int = 8
    index: int = 1
    assert add_at_index(a, num, index) is None


def test_process_add_idx() -> None:
    """Ensures that add_at_index has the desired effect"""
    a: list[int] = [7, 9, 10, 15]
    num: int = 8
    index: int = 1
    add_at_index(a, num, index)
    assert a == [7, 8, 9, 10, 15]


import pytest


def test_edge_add_idx() -> None:
    """Ensures correct value is returned on an invalid index"""
    a: list[int] = [1, 4]
    num: int = 8
    index: int = 4
    with pytest.raises(IndexError):
        add_at_index(a, num, index)
