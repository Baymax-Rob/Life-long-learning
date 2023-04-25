# Einstein

Even if you haven’t studied physics (recently or ever!), you might have heard that **E = mc^2**, wherein **E** represents energy (measured in Joules), **m** represents mass (measured in kilograms), and **c** represents the speed of light (measured approximately as 300000000 meters per second), per Albert Einstein et al. Essentially, the formula means that mass and energy are equivalent.

In a file called `einstein.py`, implement a program in Python that prompts the user for mass as an integer (in kilograms) and then outputs the equivalent number of Joules as an integer. Assume that the user will input an integer.

## Demo

```bash
$ python einstein.py
m: 50
E: 4500000000000000000
```

### Hints

- Recall that `input` returns a `str`, per docs.python.org/3/library/functions.html#input.
- Recall that `int` can convert a `str` to an `int`, per docs.python.org/3/library/functions.html#int.
- Recall that Python comes with several built-in functions, per docs.python.org/3/library/functions.html.

## How to Test

Here’s how to test your code manually:

- Run your program with `python einstein.py`. Type 1 and press Enter. Your program should output:

```bash
90000000000000000
```

- Run your program with `python einstein.py`. Type 14 and press Enter. Your program should output:

```bash
1260000000000000000
```

- Run your program with `python einstein.py`. Type 50 and press Enter. Your program should output

```bash
4500000000000000000