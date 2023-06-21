# Outdated

In the United States, dates are typically formatted in month-day-year order (MM/DD/YYYY), otherwise known as middle-endian order, which is arguably bad design. Dates in that format can’t be easily sorted because the date’s year comes last instead of first. Try sorting, for instance, `2/2/1800`, `3/3/1900`, and `1/1/2000` chronologically in any program (e.g., a spreadsheet). Dates in that format are also ambiguous. Harvard was founded on September 8, 1636, but 9/8/1636 could also be interpreted as August 9, 1636!

Fortunately, computers tend to use ISO 8601, an international standard that prescribes that dates should be formatted in year-month-day (YYYY-MM-DD) order, no matter the country, formatting years with four digits, months with two digits, and days with two digits, “padding” each with leading zeroes as needed.

In a file called `outdated.py`, implement a program that prompts the user for a date, anno Domini, in month-day-year order, formatted like`9/8/1636` or `September 8, 1636`, wherein the month in the latter might be any of the values in the `list` below:

```python
[
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
```

Then output that same date in `YYYY-MM-DD` format. If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.

## Hints

- Recall that a `str` comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods, including `split`.
- Recall that a `list` comes with quite a few methods, per docs.python.org/3/tutorial/datastructures.html#more-on-lists, among which is `index`.
- Note that you can format an `int` with leading zeroes with code like

```python
print(f"{n:02}")
```

wherein, if `n` is a single digit, it will be prefixed with one `0`, per docs.python.org/3/library/string.html#format-string-syntax.

## Demo

```bash
$ python outdated.py
Date: 9/8/1636
1636-09-8
$ python outdated.py
Date: 8 September 1636
Date: September 8, 1636
1636-09-08
$ python outdated.py
Date: 8/9/1636
1636-08-09
$ python outdated.py
Date: 1/1/1970
1970-0101
$ python outdated.py
Date: Jan 1, 1970
Date: January 1, 1970
1970-01-01
```

## How to Test

Here’s how to test your code manually:

- Run your program with `python outdated.py`. Type 9/8/1636 and press Enter. Your program should output:

```bash
1636-09-08
```

- Run your program with `python outdated.py`. Type September 8, 1636 and press Enter. Your program should output:

```bash
1636-09-08
```

- Run your program with `python outdated.py`. Type `23/6/1912` and press Enter. Your program should reprompt the user.
- Run your program with `python outdated.py`. Type `December 80, 1980` and press Enter. Your program should reprompt the user.