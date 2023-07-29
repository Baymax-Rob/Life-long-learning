import re
import sys


def main():
    """Hacking the mainframe."""
    print(validate(input("IPv4 Address: ").strip()))


def validate(ip):
    """Return a boolean value on validation of IP."""
    try:
        address = ip.split(".", maxsplit=3)
        # Split the address into a maximum of 4 ranges.
        for iprange in address:
            # Any range that exceeds 255 will raise a False response.
            if int(iprange) > 255 or len(address) < 4:
                return False

    except ValueError:
        return False

    else:
        return True


if __name__ == "__main__":
    main()
