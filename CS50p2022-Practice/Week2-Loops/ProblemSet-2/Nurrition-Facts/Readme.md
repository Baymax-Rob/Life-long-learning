# Nutrition Facts

The U.S. Food & Drug Adminstration (FDA) offers downloadable/printable posters that “show nutrition information for the 20 most frequently consumed raw fruits … in the United States. Retail stores are welcome to download the posters, print, display and/or distribute them to consumers in close proximity to the relevant foods in the stores.”

In a file called `nutrition.py`, implement a program that prompts consumers users to input a fruit (case-insensitively) and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits, which is also available as text. Capitalization aside, assume that users will input fruits exactly as written in the poster (e.g., `strawberries`, not `strawberry`). Ignore any input that isn’t a fruit.

## Hints

- Rather than use a conditional with 20 Boolean expressions, one for each fruit, better to use a `dict` to associate a fruit with its calories!
- If `k` is a `str` and `d` is a `dict`, you can check whether `k` is a key in `d` with code like:

```python
if k in d:
    ...
```

- Take care to output the fruit’s calories, not calories from fat!

## Demp

```bash
$ python nutrition.py
Item: apple
Calories: 130
$ python nutrition.py
Item: banana
Calories: 110
$ python nutrition.py
Item: Chocolate
```

## How to Test

Here’s how to test your code manually:

- Run your program with `python nutrition.py`. Type `Apple` and press Enter. Your program should output:

```bash
Calories: 130   
```

- Run your program with `python nutrition.py`. Type `Avocado` and press Enter. Your program should output:

```bash
Calories: 50
```

- Run your program with `python nutrition.py`. Type `Sweet Cherries` and press Enter. Your program should output

```bash
Calories: 100
```

- Run your program with `python nutrition.py`. Type `Tomato` and press Enter. Your program should output nothing.
