# meal schedule
schedule = [
    {"meal": "breakfast time", "start hour": 7, "end hour": 8},
    {"meal": "lunch time", "start hour": 12, "end hour": 13},
    {"meal": "dinner time", "start hour": 18, "end hour": 19},
]

def main():
    time = input("What time is it? ")
    time = float(convert(time))

    for dict in schedule:
        if time >= float(dict["start hour"]) and time <= float(dict["end hour"]):
            print(dict["meal"])
        else:
            continue


def convert(time):
    # Hints
    h, m = time.strip().split(":")
    t = float(h) + (float(m) / 60)
    # Python f-string: https://www.freecodecamp.org/chinese/news/python-f-strings-tutorial-how-to-use-f-strings-for-string-formatting/
    return f"{t:.2f}"


if __name__ == "__main__":
    main()