import pytest
from fuel import convert, gauge

def test_convert_valid():
    assert convert("1/2") == 50
    assert convert("3/4") == 75
    assert convert("1/4") == 25
    assert convert("99/100") == 99

def test_convert_invalid():
    with pytest.raises(ValueError):
        convert("abc/def")
    with pytest.raises(ValueError):
        convert("1/2.5")
    with pytest.raises(ZeroDivisionError):
        convert("1/0")
    with pytest.raises(ValueError):
        convert("5/4")
    with pytest.raises(ValueError):
        convert("2/1")
    with pytest.raises(ValueError):
        convert("1.5/2.5")  

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"

if __name__ == "__main__":
    pytest.main()
