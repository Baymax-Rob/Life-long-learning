def main():
    """Let's make some smiley faces"""
    user_input = input("Please enter a smiley or frowney face: ").strip()
    print(convert(user_input))

def convert(user_input):
    """Convert emoticons into emojis"""
    modified_input = user_input.replace(":(", "🙁").replace(":)", "🙂")
    return modified_input

if __name__ == "__main__":
    main()