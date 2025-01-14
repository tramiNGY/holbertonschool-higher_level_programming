#!/usr/bin/python3
import random
number = random.randint(-10000, 10000)
lastdigit = number % 10
isgreater = "and is greater than 5"
isless = "and is less than 6 and not 0"
if number >= 0:
    if lastdigit > 5:
        print("Last digit of", number, "is", lastdigit, isgreater)
    elif lastdigit == 0:
        print("Last digit of", number, "is", lastdigit, "and is 0")
    elif 0 < lastdigit < 6:
        print("Last digit of", number, "is", lastdigit, isless)
else:
    if lastdigit == 0:
        print("Last digit of", number, "is", lastdigit, "and is 0")
    else:
        print("Last digit of", number, "is", - (10 - lastdigit), isless)
