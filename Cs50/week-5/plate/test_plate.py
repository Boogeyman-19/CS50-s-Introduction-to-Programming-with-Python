from plates import is_valid

def test_valid_plates():
    assert is_valid("ABC123") == True
    assert is_valid("XYZ456") == True
    assert is_valid("HARV15") == True
    assert is_valid("CS50") == True
    assert is_valid("NRVOUS") == True

def test_invalid_length():
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False

def test_invalid_start():
    assert is_valid("1AB123") == False
    assert is_valid("A1B123") == False

def test_invalid_characters():
    assert is_valid("AB C12") == False
    assert is_valid("AB.C12") == False
    assert is_valid("AB#C12") == False

def test_invalid_number_position():
    assert is_valid("AB12C3") == False
    assert is_valid("AB123C") == False

def test_leading_zero():
    assert is_valid("AB0123") == False

if __name__ == "__main__":
    import pytest
    pytest.main()

