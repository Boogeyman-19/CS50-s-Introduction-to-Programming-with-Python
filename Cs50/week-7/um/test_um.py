import pytest
from um import count

def test_count_um():
    assert count("hello, um, world") == 1
    assert count("hello, Um, world") == 1
    assert count("hello, uM, world") == 1
    assert count("hello, UM, world") == 1

def test_count_no_um():
    assert count("hello, yummy, world") == 0
    assert count("hello, umm, world") == 0
    assert count("hello, ummy, world") == 0

def test_count_multiple_um():
    assert count("hello, um, um, world") == 2
    assert count("hello, Um, uM, UM, world") == 3
