# Fuel Gauge

Fuel gauges indicate, often with fractions, just how much fuel is in a tank. For instance 1/4 indicates that a tank is 25% full, 1/2 indicates that a tank is 50% full, and 3/4 indicates that a tank is 75% full.

In a file called `fuel.py`, implement a program that prompts the user for a fraction, formatted as `X/Y`, wherein each of `X` and `Y` is an integer, and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. If, though, 1% or less remains, output `E` instead to indicate that the tank is essentially empty. And if 99% or more remains, output `F` instead to indicate that the tank is essentially full.

If, though, `X` or `Y` is not an integer, `X` is greater than `Y`, or `Y` is `0`, instead prompt the user again. (It is not necessary for `Y` to be `4`.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.

## Hints

- Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods, including split.
- Note that you can handle two exceptions separately with code like:
  
```python
try:
    ...
except ValueError:
    ...
except ZeroDivisionError:
    ...
```

Or you can handle two exceptions together with code like:

```python
try:
    ...
except (ValueError, ZeroDivisionError):
    ...
```

## Demo

```bash
$ python fuel.py
Fraction: cat/dog
Fraction: 1/4
25%
$ python fuel.py
Fraction: 1/2
50%
$ python fuel.py
Fraction: 3/4
75%
$ python fuel.py
Fraction: 4/4
$ python fuel.py
Fraction: 1/0
Fraction: 0/1
E
```

## How to Test

Here’s how to test your code manually:

- Run your program with `python fuel.py`. Type `3/4` and press Enter. Your program should output:

```bash
75% 
```

- Run your program with python fuel.py. Type `1/4` and press Enter. Your program should output:

```bash
25%
```

- Run your program with `python fuel.py`. Type `4/4` and press Enter. Your program should output:
F
- Run your program with `python fuel.py`. Type `0/4` and press Enter. Your program should output:
  
```basg
E
```

- Run your program with `python fuel.py`. Type `4/0` and press Enter. Your program should handle a `ZeroDivisionError` and prompt the user again.

- Run your program with `python fuel.py`. Type three/four and press Enter. Your program should handle a `ValueError` and prompt the user again.
- Run your program with `python fuel.py`. Type `1.5/3` and press Enter. Your program should handle a `ValueError` and prompt the user again.
- Run your program with `python fuel.py`. Type `5/4` and press Enter. Your program should prompt the user again.