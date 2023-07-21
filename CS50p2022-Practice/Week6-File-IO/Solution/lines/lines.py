import sys
import os


def main():
    """Count the lines of code in a python file."""
    if len(sys.argv) < 2:
        print("Too few command-line arguments")
        sys.exit(1)
    elif len(sys.argv) > 2:
        print("Too many command-line arguments")
        sys.exit(1)
    elif not os.path.isfile(sys.argv[1]):
        print("File does not exist")
        sys.exit(1)
    elif not sys.argv[1].endswith(".py"):
        print("Not a Python file")
        sys.exit(1)
    else:
        print(counter(sys.argv[1]))


def counter(python_file):
    """Count lines of code, include doc-strings.
    Omit, blank lines and lines that start with comments."""
    ignored_lines = 0

    with open(python_file, "r") as lines:

        # Get the total line-count.
        total_lines = list(enumerate(lines.readlines(), start=1))

        # Go over every line and see it counts as code.
        for line_number, lines in total_lines:
            if (
                lines.strip().startswith("#")
                or lines.strip().startswith("\n")
                or lines.isspace()
            ):
                ignored_lines += 1

    return int(total_lines[-1][0]) - ignored_lines


if __name__ == "__main__":
    main()
