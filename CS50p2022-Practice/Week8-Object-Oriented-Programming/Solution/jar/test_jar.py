import pytest
from jar import Jar


def test_init():
    """Check that the class correctly initializes an instance object, manually and automatically"""
    grandmas_cookie_jar = Jar(9000, 8999)
    assert grandmas_cookie_jar.capacity == 9000
    assert grandmas_cookie_jar.size == 8999

    jar = Jar()
    assert jar.capacity == 12
    assert jar.size == 0


def test_capacity():
    """Check if the class correctly initializes the jar capacity."""
    chocolate_cookie_jar = Jar()
    crunchy_cookie_jar = Jar(10)

    assert crunchy_cookie_jar.capacity == 10
    assert chocolate_cookie_jar.capacity == 12

    # Check that Jar capacity can not be manually instantiated with negative integer values.
    with pytest.raises(ValueError):
        double_fudge_brownies = Jar(-1)

    with pytest.raises(ValueError):
        double_fudge_brownies = Jar("dog")


def test_size():
    """Check if the class correctly initializes a new jar to 0 cookies."""
    chocolate_cookie_jar = Jar()
    crunchy_cookie_jar = Jar()

    assert crunchy_cookie_jar.size == 0
    assert chocolate_cookie_jar.size == 0

    # Check that Jar size can not be manually instantiated with negative integer values.
    with pytest.raises(ValueError):
        double_fudge_brownies = Jar(12, -1)


def test_deposit():
    """Check if deposit adds the correct amount of cookies to the jar."""
    crunchy_cookie_jar = Jar(10)
    crunchy_cookie_jar.deposit(4)
    assert crunchy_cookie_jar.size == 4

    double_fudge_brownies = Jar(12, 11)
    with pytest.raises(ValueError):
        double_fudge_brownies.deposit(2)


def test_withdraw():
    """Check if withdraw removes the correct amount of cookies from the jar."""
    fudge_cookie_jar = Jar(4)
    fudge_cookie_jar.deposit(3)
    fudge_cookie_jar.withdraw(2)
    assert fudge_cookie_jar.size == 1

    double_fudge_brownies = Jar(12, 11)
    with pytest.raises(ValueError):
        double_fudge_brownies.withdraw(12)


def test_str():
    """Check if __str__ correctly returns the number of cookies in the jar as cookie emojis."""
    jar = Jar()
    assert str(jar) == ""

    jar.deposit(1)
    assert str(jar) == "🍪"

    jar.deposit(3)
    assert str(jar) == "🍪🍪🍪🍪"

    jar.withdraw(1)
    assert str(jar) == "🍪🍪🍪"


def test_capacity_property():
    """Check that the capacity property decorator returns the total capacity of the instance."""
    pecan_cookie_jar = Jar(24)
    assert pecan_cookie_jar.capacity == 24


def test_size_property():
    """Check that the size property decorator returns the total size of the instance."""
    coconut_cookie_jar = Jar(32)
    coconut_cookie_jar.deposit(32)
    coconut_cookie_jar.withdraw(12)
    assert coconut_cookie_jar.size == 20
