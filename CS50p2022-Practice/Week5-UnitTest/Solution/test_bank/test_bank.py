from bank import value


def test_value_casesensitivity():
    """Returns 0 if input starts with “hello”, case-insensitively."""
    assert value("hello") == 0
    assert value("Hello") == 0


def test_value_firstletter():
    """Returns 20 if input starts with an “h” (but not “hello”)."""
    assert value("howdy") == 20
    assert value("Hail Zog!") == 20


def test_value_failure():
    """Returns 100 otherwise."""
    assert value("whashappenin?") == 100
    assert value("1# Customer!") == 100
