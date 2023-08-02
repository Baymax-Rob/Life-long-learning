import sys
from attr import validate
import inflect
from datetime import datetime, date, timedelta


class DOB:
    """A Date of Birth class that takes a user's birthday in YYYY-MM-DD format."""

    def __init__(self, birthdate=0):
        self.birthdate = self.validate(birthdate)
        self.now = self.current_time()
        self.time = self.time_delta()

    def __str__(self):
        """Return the birthdate of this instance as a string."""
        return str(self.time)

    def validate(self, birthdate):
        """Validate a YYYY-MM-DD format birthdate and create an instance."""
        if birthdate == 0:
            birthdate = input("Date of Birth: ").strip()

        try:
            if date := datetime.strptime(birthdate, "%Y-%m-%d"):
                birthdate = datetime.combine(date, datetime.min.time())
                return birthdate
        except ValueError:
            sys.exit("Invalid Date")

    def current_time(self):
        """Get's the current time the program is run and modifies the time to be midnight."""
        now = datetime.combine(date.today(), datetime.min.time())
        return now

    def time_delta(self):
        """Return the time delta in minutes as an integer."""
        td = self.now - self.birthdate
        time = int(td / timedelta(minutes=1))
        return time


def main():
    seasons = DOB()
    print(sing(seasons))


def sing(minutes: int) -> int:
    """Use inflect to return a string of words that represent the input in minutes."""
    p = inflect.engine()
    lyrics = p.number_to_words(minutes, andword="")
    lyrics = f"{lyrics} minutes".capitalize()
    return lyrics


if __name__ == "__main__":
    main()
