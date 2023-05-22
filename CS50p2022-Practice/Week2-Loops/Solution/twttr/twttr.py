# Record
vowels = ["a", "e", "i", "o", "u"]

def main():
    user_text = input("Input: ").strip
    print(f"Output: {vwlrmvr(user_text)}")

def vwlrmvr(input):
    new_string = ""
    for letter in input:
    # str.lower():Return a copy of the string with all the cased characters converted to lowercase.
        if letter.lower() not in vowels:
            new_string += letter
    return new_string

if __name__ == "__main__":
    main()