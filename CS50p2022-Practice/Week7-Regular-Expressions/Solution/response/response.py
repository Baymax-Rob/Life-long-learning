import validators


def main():
    """You've got mail!"""
    print(validate(input("What's your email address? ").strip()))


def validate(address):
    """Check if email address is valid."""
    if validators.email(address):
        return "Valid"
    else:
        return "Invalid"


if __name__ == "__main__":
    main()
