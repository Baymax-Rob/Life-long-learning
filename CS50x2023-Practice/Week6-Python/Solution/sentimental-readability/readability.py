# TODO:import get_string from cs50 library
from cs50 import get_string

# prompt user for text
text = get_string("Text: ")

sent = word = letter = 0

# count the number of letters, words, and sentences in the text
for c in text:
    if c == " ":  # check for words
        word += 1
    elif c == "." or c == "?" or c == "!":  # check for sentences
        sent += 1
    elif c.lower() >= "a" and c.lower() <= "z":  # check for digits
        letter += 1

word += 1  # increasing word by one to correct it

L = (letter * 100) / word  # average letters per 100 words
S = (sent * 100) / word  # average sentences per 100 words
grade = round((0.0588 * L) - (0.296 * S) - 15.8) # Recall that the Coleman-Liau index is computed as 0.0588 * L - 0.296 * S - 15.8

# Grade X" where X is the grade level computed by the Coleman-Liau formula, rounded to the nearest integer.
if grade >= 1 and grade < 16:
    print(f"Grade {grade}")
elif grade >= 16:
    print("Grade 16+")
else:
    print("Before Grade 1")