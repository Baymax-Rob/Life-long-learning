from random import randint


# These are the values our levels represent
levelguide = [{1: [0, 9]}, {2: [10, 99]}, {3: [100, 999]}]


def main():
    """"""
    selected_level = get_level()
    problem_sets = generate_integer(selected_level)

    solved = 0

    # Ask the user each question in the randomly generated problem set
    for question in problem_sets:
        attempts = 0

        while True:
            try:
                useranswer = int(input(f"{question} = "))
                a, b = question.strip(" ").split("+")

                # Compare the user's answer to the actual answer
                if attempts == 2:
                    print("EEE")
                    print(f"{question} = {(int(a) + int(b))}")
                    break
                elif useranswer != (int(a) + int(b)):
                    attempts += 1
                    print("EEE")
                else:
                    solved += 1
                    attempts = 0
                    break

            # Catches user trying to enter words instead of numbers
            except ValueError:
                print("EEE")
                attempts += 1
                continue

    print(f"Score: {solved}")


def get_level():
    """Get the user's preferred difficulty level"""
    while True:
        try:
            level = int(input("Level: "))
            # If the level falls outside 1 - 3, prompt the user again
            if level <= 3 and level > 0:
                return level

        except ValueError:
            continue


def generate_integer(level):
    """Generate 10 randomized problems where each level represents x digits"""
    problem_set = []

    # get the appropriate difficulty from the levelguide
    rint_lo = levelguide[level - 1][level][0]
    rint_hi = levelguide[level - 1][level][1]

    # build a list of problem sets based off of the user's input
    for _ in range(0, 10):
        problem_set.append(f"{randint(rint_lo, rint_hi)} + {randint(rint_lo, rint_hi)}")

    return problem_set


if __name__ == "__main__":
    main()
