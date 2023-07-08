vowels = ["a", "e", "i", "o", "u"]


def main():
    """Smwhr vr th rnbw!"""
    word = str(input("Input: ").strip())
    print(f"Output: {shorten(word)}")


def shorten(word):
    """Rmvs ll vwls"""
    new_string = ""
    # Goes through every letter in the word.
    for letter in word:
        if letter.lower() not in vowels:
            new_string += letter

    return new_string


if __name__ == "__main__":
    main()
