menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00,
}

def main():
    orders = 0
    while True:
        # Make user input case insensitive and print total
        try:
            item = input("Item: ").strip().title()
            if item in menu:
                orders += menu[item]
                print(f"${orders:.2f}")
        # Enter CTRL+D to end the session
        except (EOFError, KeyError):
            print("", end="\n")
            quit()

if __name__ == "__main__":
    main()