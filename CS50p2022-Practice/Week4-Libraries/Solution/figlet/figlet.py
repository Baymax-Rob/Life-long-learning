import sys
from random import choice
from pyfiglet import Figlet


def main():
    """
       ___________ __________  ____
      / ____/ ___// ____/ __ \/ __ \
     / /    \__ \/___ \/ / / / /_/ /
    / /___ ___/ /___/ / /_/ / ____/
    \____//____/_____/\____/_/
    Let's get crafty!
    """
    f = Figlet()
    available_fonts = f.getFonts()

    # In the case of no parameters passed to argv, do this.
    if len(sys.argv) == 1:
        s = input("Input: ").strip()
        f.setFont(font=choice(available_fonts))
        print(f.renderText(s))

    # In the case of correctly flagged parameters passed, do this.
    elif len(sys.argv) == 3:
        if str(sys.argv[1]) in ["-f", "--font"] and str(sys.argv[2]) in available_fonts:
            s = input("Input: ").strip()
            f.setFont(font=str(sys.argv[2]))
            print(f.renderText(s))
        else:
            sys.exit("Invalid usage")

    # Not good!
    else:
        sys.exit("Invalid usage")


if __name__ == "__main__":
    main()
