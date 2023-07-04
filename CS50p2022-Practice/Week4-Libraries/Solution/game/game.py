from random import randint


def main():
    """Loser buys lunch!, Let's gooo!"""
    while True:

        # Prompt the user to select a level to guess under.
        try:
            userrange = int(input("Level: ").strip())

            # Check for a positive integer in level.
            if userrange >= 1:
                guessme = randint(1, userrange)
                guessed(guessme)
                break

        # Reprompt the user on Type or Value Errors.
        except (TypeError, ValueError):
            continue


def guessed(gennum):
    """Check if the userguess is correct"""
    while True:
        userguess = int(input("Guess: ").strip())

        # Check if the guess is too big or too small.
        try:
            if userguess > gennum:
                print("Too large!")
            elif userguess < gennum:
                print("Too small!")
            else:
                print("Just right!")
                break

        # Reprompt the user on Type or Value Errors.
        except (TypeError, ValueError):
            continue


if __name__ == "__main__":
    main()
