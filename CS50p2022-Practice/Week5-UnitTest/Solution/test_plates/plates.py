def main():
    """Stand in line at the DMV?"""
    plate = input("Plate: ").strip()
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    """2cool4Skool"""
    s = str(s)

    validated = ""
    numcheck = 0

    illegal_symbols = [
        " ",
        ".",
        "?",
        "!",
        ",",
        ":",
        ";",
        "(",
        ")",
        "[",
        "]",
        "'",
        "-",
        '"',
        "/",
        "\\",
        "`",
        "@",
        "#",
        "*",
    ]
    # “Numbers cannot be used in the middle of a plate; they must come at the end. For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. The first number used cannot be a ‘0’.”
    # “No periods, spaces, or punctuation marks are allowed.”

    # Check the following rules to validate the input
    if len(s) >= 2 and len(s) <= 6:
        if s[0].isalpha() and s[1].isalpha():
            for ch in s:
                if ch not in illegal_symbols:
                    if ch.isnumeric() and numcheck == 0 and ch != "0":
                        numcheck += 1
                        validated += ch
                    elif ch.isnumeric() and numcheck > 0:
                        numcheck += 1
                        validated += ch
                    elif ch.isalpha() and numcheck < 1:
                        validated += ch
    else:
        return False

    # Let the caller know what's up
    if validated == s:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
