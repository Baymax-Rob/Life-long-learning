# Pizza Py

Perhaps the most popular place for pizza in Harvard Square is Pinocchio’s Pizza & Subs, aka Noch’s, known for its Sicilian pizza, which is “a deep-dish or thick-crust pizza.”

Students tend to buy pizza by the slice, but Pinocchio’s also has whole pizzas on its menu too, per this CSV file of Sicilian pizzas, `sicilian.csv`, below:

```bash
Sicilian Pizza,Small,Large
Cheese,$25.50,$39.95
1 item,$27.50,$41.95
2 items,$29.50,$43.95
3 items,$31.50,$45.95
Special,$33.50,$47.95
```

See `regular.csv` for a CSV file of regular pizzas as well.

Of course, a CSV file isn’t the most customer-friendly format to look at. Prettier might be a table, formatted as ASCII art, like this one:

+------------------+---------+---------+
| Sicilian Pizza   | Small   | Large   |
+==================+=========+=========+
| Cheese           | $25.50  | $39.95  |
+------------------+---------+---------+
| 1 item           | $27.50  | $41.95  |
+------------------+---------+---------+
| 2 items          | $29.50  | $43.95  |
+------------------+---------+---------+
| 3 items          | $31.50  | $45.95  |
+------------------+---------+---------+
| Special          | $33.50  | $47.95  |
+------------------+---------+---------+
In a file called `pizza.py`, implement a program that expects exactly one command-line argument, the name (or path) of a CSV file in Pinocchio’s format, and outputs a table formatted as ASCII art using `tabulate`, a package on PyPI at pypi.org/project/tabulate. Format the table using the library’s grid format. If the user does not specify exactly one command-line argument, or if the specified file’s name does not end in `.csv`, or if the specified file does not exist, the program should instead exit via `sys.exit`.

## Hints

- Recall that the `csv` module comes with quite a few methods, per docs.python.org/3/library/csv.html, among which are `reader`, per docs.python.org/3/library/csv.html#csv.reader, and `DictReader`, per docs.python.org/3/library/csv.html#csv.DictReader.
- Note that `open` can `raise` a `FileNotFoundError`, per docs.python.org/3/library/exceptions.html#FileNotFoundError.
- Note that the `tabulate` package comes with just one function, per pypi.org/project/tabulate. You can install the package with:

```bash
pip install tabulate
```

## Demo

```
$ python pizza.py                                                               
Too few command-line arguments                                                  
$ python pizza.py foo                                                           
Not a CSV file                                                                  
$ python pizza.py foo bar                                                       
Too many command-line arguments 
$ python pizza.py sicilian.csv
+------------------+---------+---------+                                        
| Sicilian Pizza   | Small   | Large   |                                        
+==================+=========+=========+                                        
| Cheese           | $25.50  | $39.95  |                                        
+------------------+---------+---------+                                        
| 1 item           | $27.50  | $41.95  |                                        
+------------------+---------+---------+                                        
| 2 items          | $29.50  | $43.95  |                                        
+------------------+---------+---------+                                        
| 3 items          | $31.50  | $45.95  |                                        
+------------------+---------+---------+                                        
| Special          | $33.50  | $47.95  |                                        
+------------------+---------+---------+
$ python pizza.py regular.csv                                                   
+-----------------+---------+---------+                                         
| Regular Pizza   | Small   | Large   |                                         
+=================+=========+=========+                                         
| Cheese          | $13.50  | $18.95  |                                         
+-----------------+---------+---------+                                         
| 1 topping       | $14.75  | $20.95  |                                         
+-----------------+---------+---------+                                         
| 2 toppings      | $15.95  | $22.95  |                                         
+-----------------+---------+---------+                                         
| 3 toppings      | $16.95  | $24.95  |                                         
+-----------------+---------+---------+                                         
| Special         | $18.50  | $26.95  |                                         
+-----------------+---------+---------+
```

## How to Test

Here’s how to test your code manually:

- Run your program with python pizza.py. Your program should exit using sys.exit and provide an error message:

```bash
Too few command-line arguments
```

- Be sure to download `regular.csv` and `sicilian.csv`, placing them in the same folder as pizza.py. Run your program with python pizza.py regular.csv `sicilian.csv`. Your program should output:
Too many command-line arguments
- Run your program with `python pizza.py invalid_file.csv`. Assuming `invalid_file.csv` doesn’t exist, your program should exit using sys.exit and provide an error message:

```bash
File does not exist
```

- Create a file named `sicilian.txt`. Run your program with `python pizza.py sicilian.txt`. Your program should exit using `sys.exit` and provide an error message:
  
```bash
Not a CSV file
```

- Run your program with `python pizza.py regular.csv`. Assuming you’ve downloaded `regular.csv`, your program should print a table like the below:
  
```bash
+-----------------+---------+---------+
| Regular Pizza   | Small   | Large   |
+=================+=========+=========+
| Cheese          | $13.50  | $18.95  |
+-----------------+---------+---------+
| 1 topping       | $14.75  | $20.95  |
+-----------------+---------+---------+
| 2 toppings      | $15.95  | $22.95  |
+-----------------+---------+---------+
| 3 toppings      | $16.95  | $24.95  |
+-----------------+---------+---------+
| Special         | $18.50  | $26.95  |
+-----------------+---------+---------+
```

