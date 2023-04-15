# TODO: import get_string from cs50 library
from cs50 import get_int, get_string

while True:
    number = get_int("Number: ")
    if (number >= 0):
        break

tmp = number
sum = 0
i = 0

while number > 0:
    digit = number % 10 # stores the last digit of the number
    if (i % 2 == 0):
        sum += digit
    else:
        if (digit * 2 >= 10):
            sum += digit * 2 // 10
            sum += digit * 2 % 10
        else:
            sum += digit * 2
    number = number // 10
    i += 1

number = tmp

if (sum % 10 == 0): # checks if last number of the total sum is 0
    if (number // 10000000000000 == 34 or number // 10000000000000 == 37):
        print("AMEX")
    elif (number // 100000000000000 >= 51 and number // 100000000000000 <= 55):
        print("MASTERCARD")
    elif (number // 1000000000000 == 4 or number // 1000000000000000 == 4):
        print("VISA")
    else:
        print("INVALID")
else:
    print("INVALID")