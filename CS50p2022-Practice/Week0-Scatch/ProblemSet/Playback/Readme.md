# Playback Speed

Some people have a habit of lecturing speaking rather quickly, and it’d be nice to slow them down, a la YouTube’s 0.75 playback speed, or even by having them pause between words.

In a file called `playback.py`, implement a program in Python that prompts the user for input and then outputs that same input, replacing each space with `...` (i.e., three periods).

## Demo

```bash
$ python playback.py
This is CS50.
This...is...CS50.
```

### Hints

- Recall that input returns a str, per docs.python.org/3/library/functions.html#input.
- Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.

## How to Test

Here’s how to test your code manually:

- Run your program with `python playback.py`. Type `This is CS50` and press Enter. Your program should output:

```bash
This...is...CS50    
```

- Run your program with `python playback.py`. Type `This is our week on functions` and press Enter. Your program should output:

```bash
This...is...our...week...on...functions
```

- Run your program with `python playback.py`. Type `Let's implement a function called hello` and press Enter. Your program should output

```bash
Let's...implement...a...function...called...hello
```
