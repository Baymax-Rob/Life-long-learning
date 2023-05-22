def main():
    valid_conis = [25, 10, 5]
    cost = 50
    tendered = 0

    while tendered < cost:
        print(f"Amount Due: {cost - tendered}")
        #str.strip(): Return a copy of the string with the leading and trailing characters removed.
        money = int(input(f"Insert Coni: ").strip())
        if money in valid_conis:
            tendered += money
        else:
            continue
    print(f"Change Owed: {tendered - cost"})

if __name__ == "__main__":
    main()