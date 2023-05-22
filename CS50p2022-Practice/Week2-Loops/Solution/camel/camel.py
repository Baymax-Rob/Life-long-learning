def main():
    #str.strip(): Return a copy of the string with the leading and trailing characters removed.
    # The chars argument is a string specifying the set of characters to be removed.
    # If omitted or None, the chars argument defaults to removing whitespace.
    # The chars argument is not a prefix or suffix; rather, all combinations of its values are stripped:
    case = input("camelCase: ").strip()
    print(f"snake_case: {snakeCase(case)}")


def snakeCase(input):
    snak = ""
    for letter in input:
    # str.isupper():Return True if all cased characters in the string are uppercase and there is at least one cased character, False otherwise.
        if letter.isupper():
            snak += "_"
    # str.lower():Return a copy of the string with all the cased characters converted to lowercase.
            snak += letter.lower()
        else:
            snak += letter

    return snak

if __name__ == "__main__":
    main()