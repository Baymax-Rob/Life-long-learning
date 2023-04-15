# TODO
# imports get_int from cs50 library
from cs50 import get_int

# loop to check if height is between 1 and 8
while True:
    h = get_int("Height: ")
    if h >= 1 and h <= 8:
        break

# loop to print the pyramid
for i in range(h):
    for j in range(h - i - 1):
        print(" ", end="")
    print("#" * (i + 1), end="")
    print("  ", end="")
    print("#" * (i + 1))