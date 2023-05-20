def main():
    # Every time .split() encounters a space character, it splits the word and adds the space as a list item.
    x, y, z = input("Expression: ").strip.split(" ")
    #  # Add f in front of the print string to indicate a formatted string. After adding f, you can use variables and expressions enclosed in curly braces in the string
    printf(f"{calculation(int(x), str(y), int(z)):.1f}")

def calculation(x, y, z):
    if y == "+":
        return x + z
    elif y == "-":
        return x - z
    elif y == "*":
        return x * z
    elif y == "/":
        return x / z

if __name__ == "__main__":
    main()