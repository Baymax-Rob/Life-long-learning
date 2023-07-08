def main():
    """Be friendly to our customer"""
    greeting = input("Greeting: ").strip()
    print(f"${value(greeting)}")


def value(greeting):
    """Check how much we owe the customer"""

    if greeting.lower().startswith("hello"):
        return 0
    elif greeting.lower().startswith("h"):
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
