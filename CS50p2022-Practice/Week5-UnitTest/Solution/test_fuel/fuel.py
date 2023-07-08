def main():
    """Hit the road, jack!"""
    while True:
        # How much fuel is in the tank?
        try:
            fraction = str(input("Fraction: ").strip())
            print(gauge(convert(fraction)))
            break
        except (ValueError, ZeroDivisionError, UnboundLocalError):
            continue


def convert(fraction):
    """Convert a string to a X/Y fraction with its numerator and denominator represented
    by an integer between 0 and 100, inclusive. If X or Y is not an integer, raise a ValueError.
    If Y is 0, raise a ZeroDivisionError."""
    if "/" in fraction:
        x, y = fraction.split("/", 1)
    else:
        raise UnboundLocalError("Not a valid fraction.")

    # Check that both X and Y are integers
    if x.isdigit() and y.isdigit():
        # Check that X isn't larger than Y and that Y isn't zero
        if int(x) <= int(y) and int(y) != 0:
            percentage = (int(x) / int(y)) * 100
            return percentage
        else:
            raise ZeroDivisionError("X is larger than Y")
    else:
        raise ValueError("Not an integer")


def gauge(percentage):
    """Given a percentage as an integer between 1 and 99, gauge should return fuel reserve
    as a percentage. If below 1 percent or above 99%, display 'E' or 'F', respectively."""
    if int(percentage) >= 99:
        return "F"
    elif int(percentage) < 99 and int(percentage) > 1:
        return f"{percentage:.0f}%"
    else:
        return "E"


if __name__ == "__main__":
    main()
