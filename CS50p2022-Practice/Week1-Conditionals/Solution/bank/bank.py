def main():
    greeting = input("Greeting: ").strip().lower()
    # Add f in front of the print string to indicate a formatted string. After adding f, you can use variables and expressions enclosed in curly braces in the string
    print(f"${penalty(greeting)}")

def penalty(greeting):
    if greeting.startswith("hello"):
    # If the greeting starts with “hello”, output $0
        return 0
    elif greeting.startswith("h"):
    # If the greeting starts with an “h” (but not “hello”), output $20
        return 20
    else:
    # Otherwise, output $100
        return 100

if __name__ == "__main__":
    main()