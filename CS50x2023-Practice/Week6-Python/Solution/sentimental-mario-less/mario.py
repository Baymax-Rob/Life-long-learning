# TODO
from cs50 import get_int

# loop to check if height is between 1 and 8
while True:
    height = get_int("Height: ")
    if (height >= 1 and height <= 8):
        break
# loop to print the pyramid
for i in range(height):
    print(" " * (height - i - 1), end="")
    print("#" * (i + 1))