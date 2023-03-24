# Readability

Implement a program that computes the approximate grade level needed to comprehend some text, per the below.

```sh
$ python readability.py
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
```

## Specification

- Write, in a file called `readability.py`, a program that first asks the user to type in some text, and then outputs the grade level for the text, according to the Coleman-Liau formula, exactly as you did in `Problem Set 2`, except that your program this time should be written in Python.
- Recall that the Coleman-Liau index is computed as `0.0588 * L - 0.296 * S - 15.8`, where L is the average number of letters per 100 words in the text, and S is the average number of sentences per 100 words in the text.
- Use `get_string` from the CS50 Library to get the user’s input, and `print` to output your answer.
- Your program should count the number of letters, words, and sentences in the text. You may assume that a letter is any lowercase character from `a` to `z` or any uppercase character from `A` to `Z`, any sequence of characters separated by spaces should count as a word, and that any occurrence of a period, exclamation point, or question mark indicates the end of a sentence.
- Your program should print as output "`Grade X`" where `X` is the grade level computed by the Coleman-Liau formula, rounded to the nearest integer.
- If the resulting index number is 16 or higher (equivalent to or greater than a senior undergraduate reading level), your program should output "`Grade 16+`" instead of giving the exact index number. If the index number is less than 1, your program should output "`Before Grade 1`".

## Usage

Your program should behave per the example below.

```sh
$ python readability.py
Text: Congratulations! Today is your day. You're off to Great Places! You're off and away!
Grade 3
```

## Testing

- Run your program as `python readability`.py, and wait for a prompt for input. Type in `One fish. Two fish. Red fish. Blue fish.` and press enter. Your program should output Before `Grade 1`.
- Run your program as `python readability.py`, and wait for a prompt for input. Type in `Would you like them here or there? I would not like them here or there. I would not like them anywhere`. and press enter. Your program should output `Grade 2`.
- Run your program as `python readability.py`, and wait for a prompt for input. Type in `Congratulations! Today is your day. You're off to Great Places! You're off and away!` and press enter. Your program should output `Grade 3`.
- Run your program as `python readability.py`, and wait for a prompt for input. Type in `Harry Potter was a highly unusual boy in many ways. For one thing, he hated the summer holidays more than any other time of year. For another, he really wanted to do his homework, but was forced to do it in secret, in the dead of the night. And he also happened to be a wizard`. and press enter. Your program should output `Grade 5`.
- Run your program as`python readability.py`, and wait for a prompt for input. Type in `In my younger and more vulnerable years my father gave me some advice that I've been turning over in my mind ever since`. and press enter. Your program should output `Grade 7`.
- Run your program as `python readability.py`, and wait for a prompt for input. Type in `Alice was beginning to get very tired of sitting by her sister on the bank, and of having nothing to do: once or twice she had peeped into the book her sister was reading, but it had no pictures or conversations in it, "and what is the use of a book," thought Alice "without pictures or conversation?`" and press enter. Your program should output `Grade 8`.
- Run your program as `python readability`.py, and wait for a prompt for input. Type in `When he was nearly thirteen, my brother Jem got his arm badly broken at the elbow. When it healed, and Jem's fears of never being able to play football were assuaged, he was seldom self-conscious about his injury. His left arm was somewhat shorter than his right; when he stood or walked, the back of his hand was at right angles to his body, his thumb parallel to his thigh`. and press enter. Your program should output `Grade 8`.
- Run your program as `python readability`.py, and wait for a prompt for input. Type in `There are more things in Heaven and Earth, Horatio, than are dreamt of in your philosophy`. and press enter. Your program should output `Grade 9`.
- Run your program as `python readability.py`, and wait for a prompt for input. Type in `It was a bright cold day in April, and the clocks were striking thirteen. Winston Smith, his chin nuzzled into his breast in an effort to escape the vile wind, slipped quickly through the glass doors of Victory Mansions, though not quickly enough to prevent a swirl of gritty dust from entering along with him`. and press enter. Your program should output Grade `10`.
- Run your program as `python readability.py`, and wait for a prompt for input. Type in `A large class of computational problems involve the determination of properties of graphs, digraphs, integers, arrays of integers, finite families of finite sets, boolean formulas and elements of other countable domains`. and press enter. Your program should output `Grade 16+`.