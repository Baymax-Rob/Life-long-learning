import os
import sys
from PIL import Image, ImageOps


def main():
    """Dress a puppet in a Harvard CS50 Shirt."""
    if len(sys.argv) < 3:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 3:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print(f"Invalid input - Path")
        sys.exit(1)
    elif not format_check(sys.argv[1]) and format_check(sys.argv[2]):
        print("Invalid input")
        sys.exit(1)
    elif not format_same(sys.argv[1], sys.argv[2]):
        print("Input and output have different extensions")
        sys.exit(1)
    else:
        fit_shirt(sys.argv[1], sys.argv[2])


def format_check(input_filetype):
    """Returns a boolean value if the input file has a valid format."""
    valid_formats = ["jpg", "jpeg", "png"]
    _, fn_ext = input_filetype.split(".", maxsplit=1)

    # If the format isn't valid, return False
    if fn_ext in valid_formats:
        return True
    else:
        return False


def format_same(input_file, output_file):
    """Returns a boolean value if both filepaths contain the same file format."""
    _, fn_ext = input_file.split(".", maxsplit=1)

    # If input and output don't match, return False
    if output_file.endswith(fn_ext):
        return True
    else:
        return False


def fit_shirt(input_file, output_file):
    """Import an image and overlay it onto the source image"""
    shirt = Image.open("shirt.png")
    photo = Image.open(input_file)

    # Use fit to resize and crop the source image while maintaining its aspect ratio.
    a, b = shirt.size
    photo = ImageOps.fit(photo, (a, b))

    # Paste the overlay into the source and save the output.
    photo.paste(shirt, shirt)
    photo.save(output_file)


if __name__ == "__main__":
    main()
