from numb3rs import validate
import pytest

def test_valid_ipv4():
    assert validate("192.168.1.1") == True

def test_invalid_ipv4():
    assert validate("275.3.6.28") == False

def test_invalid_format():
    assert validate("192.168.1") == False

def test_invalid_characters():
    assert validate("192.168.1.x") == False

if __name__=="__main__":
    pytest.main()
