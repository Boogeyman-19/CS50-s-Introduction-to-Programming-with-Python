import twttr
import pytest

def test_shorten():
    assert twttr.shorten("Twitter") == "Twttr"
    assert twttr.shorten("TWITTER") == "TWTTR"
    assert twttr.shorten("twitter") == "twttr"
    assert twttr.shorten("Hello, World!") == "Hll, Wrld!"
    assert twttr.shorten("1234567890") == "1234567890"
    assert twttr.shorten("") == ""
    assert twttr.shorten("AEIOUaeiou") == ""
    assert twttr.shorten("BcDfGhJkLmN") == "BcDfGhJkLmN"

if __name__ == "__main__":
    pytest.main()
