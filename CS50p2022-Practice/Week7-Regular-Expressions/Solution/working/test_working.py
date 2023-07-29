import pytest
from working import convert


def test_time_case():
    """Check that convert is case insensitive."""
    assert convert("9:00 AM to 5:00 PM") == "09:00 to 17:00"


def test_max_range():
    """Check that convert handles maximum time ranges."""
    assert convert("12:00 PM to 12:00 PM") == "12:00 to 12:00"


def test_mixed_formats():
    """Check that convert raises ValueErrors mixing 12H and 24H time."""
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")


def test_omit_to():
    """Check that convert raises ValueErrors when 'to' is omitted."""
    with pytest.raises(ValueError):
        convert(" to ")


def test_out_of_range_hours():
    """Check that convert raises ValueErrors when hour ranges are exceeded."""
    with pytest.raises(ValueError):
        convert("13:00 AM to 13:00 PM")

    with pytest.raises(ValueError):
        convert("0:00 AM to 0:00 PM")

    with pytest.raises(ValueError):
        convert("13 AM to 13 PM")

    with pytest.raises(ValueError):
        convert("0 AM to 0 PM")


def test_out_of_range_minutes():
    """Check that convert raises ValueErrors when minute ranges are exceeded."""
    with pytest.raises(ValueError):
        convert("12:61 AM to 5:60 PM")


def test_no_entry():
    """Check that convert raises ValueErrors when nothing is entered."""
    with pytest.raises(ValueError):
        convert("")


def test_invalid_format():
    """Check that convert raises ValueErrors when time values are poorly formatted."""
    with pytest.raises(ValueError):
        convert("9AM to 5PM")

    with pytest.raises(ValueError):
        convert("6:19 AM 4:20 PM")

    with pytest.raises(ValueError):
        convert("9 AM - 5 PM")
