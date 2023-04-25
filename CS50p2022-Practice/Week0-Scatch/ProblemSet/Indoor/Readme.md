# Indoor Voice

WRITING IN ALL CAPS IS LIKE YELLING.

Best to use your “indoor voice” sometimes, writing entirely in lowercase.

In a file called `indoor.py`, implement a program in Python that prompts the user for input and then outputs that same input in lowercase. Punctuation and whitespace should be outputted unchanged. You’re welcome, but not required, to prompt the user explicitly, as by passing a str of your own as an argument to input.

## Demo

```bash
$ python indoor.py
HELLO, WORLD
hello, world
```

### Hints

- Recall that input returns a str, per docs.python.org/3/library/functions.html#input.
- Recall that a str comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#string-methods.

## How to Test

Here’s how to test your code manually. At the `indoor/ $` prompt in your terminal: :

- Run your program with `python indoor.py`. Type `HELLO` and press Enter. Your program should output hello.
- Run your program with `python indoor.py`. Type `THIS IS CS50` and press Enter. Your program should output `this is cs50`.
- Run your program with `python indoor.py`. Type `50` and press Enter. Your program should output `50`.
If you run into an error saying your file cannot be opened, retrace your steps to be sure that you are inside your `indoor` folder and have saved your `indoor.py` file there. Remember how?