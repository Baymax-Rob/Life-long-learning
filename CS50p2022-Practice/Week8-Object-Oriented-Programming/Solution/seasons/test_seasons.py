import pytest
from seasons import DOB, sing


def test_init():
    """"""
    testuser = DOB("2000-01-01")
    assert str(testuser.birthdate) == "2000-01-01 00:00:00"
    assert str(testuser) == "11796480"


def test_sing():
    """"""
    testuser2 = DOB("2000-01-01")
    assert (
        sing(testuser2)
        == "Eleven million, seven hundred ninety-six thousand, four hundred eighty minutes"
    )


def test_invalid_date():
    """"""
    with pytest.raises(SystemExit):
        DOB("2000-13-13")
