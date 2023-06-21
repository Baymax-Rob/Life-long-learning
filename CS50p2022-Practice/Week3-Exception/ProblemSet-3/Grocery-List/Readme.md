# Grocery List

Suppose that you’re in the habit of making a list of items you need from the grocery store.

In a file called `grocery.py`, implement a program that prompts the user for items, one per line, until the user inputs control-d (which is a common way of ending one’s input to a program). Then output the user’s grocery list in all uppercase, sorted alphabetically by item, prefixing each line with the number of times the user inputted that item. No need to pluralize the items. Treat the user’s input case-insensitively.

## Hints

- Note that you can detect when the user has inputted control-d by catching an EOFError with code like:

```python
try:
    item = input()
except EOFError:
    ...
```

- Odds are you’ll want to store your grocery list as a `dict`.
- Note that a `dict` comes with quite a few methods, per docs.python.org/3/library/stdtypes.html#mapping-types-dict, among them get, and supports operations like:
  
```python
d[key]
```

and

```python
if key in d:
    ...
```

wherein d is a dict and key is a str.

Be sure to avoid or catch any KeyError.

## Demo

```bash
$ python grocery.py
apple
banana
banana
ice cream

1 APPLE
2 BANANA
3 ICE CREAM
$ python grocery.py
lettuce
tomato
tomato
carrot
tomato

1 CARROT
2 LETTUCE
3 TOMATO
```

## How to Test

Here’s how to test your code manually:

- Run your program with `python grocery.py`. Type `mango` and press Enter, then type `strawberry` and press Enter, followed by control-d. Your program should output:

```bash
1 MANGO
1 STRAWBERRY
```

- Run your program with `python grocery.py`. Type `milk` and press Enter, then type `milk` again and press Enter, followed by control-d. Your program should output:

```bash
2 MILK
```

- Run your program with `python grocery.py`. Type `tortilla` and press Enter, then type sweet `potato` and press Enter, followed by control-d. Your program should output:

```bash
1 SWEET POTATO
1 TORTILLA
```