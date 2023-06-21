def main():
    grolist = []
    while True:
        # Make a list of all the goodies
        try:
            item = input().strip().lower()
            grolist.append(item)
        # Catch CTRL+D to end the session
        except (EOFError, KeyError):
            l = sorted(set(grolist))
            for i in l:
                print(f"{grolist.count(i)} {i.upper()}")
            quit()

main()