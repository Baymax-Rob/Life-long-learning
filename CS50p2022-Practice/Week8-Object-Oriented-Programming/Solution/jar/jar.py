class Jar:
    """A jar full of cookies!"""

    def __init__(self, capacity=12, size=0):
        """Initialize the Jar object"""
        self.capacity = capacity
        self.size = size

    def __str__(self):
        """Print a string containing n cookies in the jar."""
        return "🍪" * self.size

    def deposit(self, n):
        """Add n number of cookies to the jar."""
        if not n > (self.capacity - self.size):
            self.size += n
        else:
            raise ValueError("Too many cookies!")

    def withdraw(self, n):
        """Remove n number of cookies to the jar."""
        if not n > self.size:
            self.size -= n
        else:
            raise ValueError("Too few cookies!")

    @property
    def capacity(self):
        """Getter returns the total capacity of the cookie jar."""
        return self._capacity

    @property
    def size(self):
        """Getter returns the number of cookies in the cookie jar."""
        return self._size

    @capacity.setter
    def capacity(self, capacity):
        """"""
        if not int(capacity) > 0:
            raise ValueError("Not a non-negative integer.")
        self._capacity = capacity

    @size.setter
    def size(self, size):
        """"""
        if int(size) < 0:
            raise ValueError
        else:
            self._size = size


def main():
    """Omnomnomnomnom!"""
    cookies = Jar(13)
    cookies.deposit(13)
    cookies.withdraw(13)
    print(cookies.capacity)
    print(cookies.size)


if __name__ == "__main__":
    main()
