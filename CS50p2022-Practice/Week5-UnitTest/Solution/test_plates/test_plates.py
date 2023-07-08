from plates import is_valid


def test_startwith():
    """Vanity plates must start with at least two letters."""
    assert is_valid("1") == False
    assert is_valid("22") == False
    assert is_valid("AA") == True


def test_minmax():
    """Vanity plates may contain a maximum of 6 characters and a minimum of 2 characters."""
    assert is_valid("A") == False
    assert is_valid("ABCDEFG") == False
    assert is_valid("ABCDEF") == True


def test_numbers():
    """Numbers cannot be used in the middle of a plate; they must come at the end."""
    assert is_valid("123456") == False
    assert is_valid("123ABC") == False
    assert is_valid("XYZ012") == False
    assert is_valid("AB12C3") == False
    assert is_valid("AB12CA") == False
    assert is_valid("ABC123") == True


def test_blockedsymbols():
    """No periods, spaces, or punctuation marks are allowed."""
    assert is_valid("ABC?!-") == False
    assert is_valid(". 12[]") == False
    assert is_valid("/B^D3*") == False
