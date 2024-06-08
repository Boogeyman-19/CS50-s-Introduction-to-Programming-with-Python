import pytest
from bank import value

def test_value_hello():
    assert value("hello") == 0
    assert value("Hello") == 0
    assert value("HELLO") == 0

def test_value_h():
    assert value("h") == 20
    assert value("h123") == 20
    assert value("h!@#") == 20

def test_value_other():
    assert value("bye") == 100
    assert value("123") == 100
    assert value("!@#") == 100
