import pytest
from fuel import convert, gauge


def test_convert():
    """Convert a string to a X/Y fraction with its numerator and denominator represented
    by an integer between 0 and 100, inclusive."""
    assert convert("0/1") == 0
    assert convert("1/1") == 100
    assert convert("1/2") == 50
    assert convert("1/100") == 1

    # Check if code catches attempted zero division
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

    # Check if code catches non-integers
    with pytest.raises(ValueError):
        convert("x/y")


def test_gauge():
    """Given a percentage as an integer between 1 and 99, gauge should return fuel reserve
    as a percentage. If below 1 percent or above 99%, display 'E' or 'F', respectively."""
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(2) == "2%"
    assert gauge(50) == "50%"
    assert gauge(98) == "98%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"
