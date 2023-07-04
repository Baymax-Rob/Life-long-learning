import inflect


def main():
    """Let's bid them all adieu!"""
    p = inflect.engine()
    mylist = []

    while True:

        # Get input from the user
        try:
            user_input = str(input("Name: ")).strip()
            mylist.append(user_input)
        # Catch CTRL+D to end the session
        except (EOFError, KeyError):
            print(f"Adieu, adieu, to {p.join(mylist)}", end="\n")
            quit()


if __name__ == "__main__":
    main()
