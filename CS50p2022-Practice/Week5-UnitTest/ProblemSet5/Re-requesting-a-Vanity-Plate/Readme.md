# Testing my twttr

In a file called `plates.py`, reimplement Vanity Plates from Problem Set 2, restructuring your code per the below, wherein `is_valid` still expects a `str` as input and returns `True` if that str meets all requirements and `False` if it does not, but `main` is only called if the value of __name__ is "__main__":

```python
def main():
    ...


def is_valid(s):
    ...


if __name__ == "__main__":
    main()
```

Then, in a file called `test_plates.py`, implement **four or more** functions that collectively test your implementation of `is_valid` thoroughly, each of whose names should begin with `test_` so that you can execute your tests with:

```bash
pytest test_plates.py
```

### Hints

- Be sure to include

```python
import plates
```

or

```python
from plates import is_valid
```

atop `test_plates.py` so that you can call `is_valid` in your tests.

Take care to `return`, not `print`, a `bool` in `is_valid`. Only `main` should call `print`.

## How to Test

To test your tests, run `pytest test_plates.py`. Be sure you have a copy of a `plates.py` file in the same folder. Try to use correct and incorrect versions of plates.py to determine how well your tests spot errors:

- Ensure you have a correct version of `plates.py`. Run your tests by executing `pytest test_plates.py`. pytest should show that all of your tests have passed.
- Modify the correct version of `plates.py`, perhaps eliminating some of its constraints. Your program might, for example, mistakenly print “Valid” for a license plate of any length! Run your tests by executing `pytest test_plates.py`. `pytest` should show that at least one of your tests has failed.