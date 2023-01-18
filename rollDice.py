# Exercise #17: Dice Roll

import random
from time import sleep

# By the book solution :
# def rollDice(numberOfDice):
#     roll = 0
#     for n in range(0, numberOfDice):
#         roll += random.randint(1, 6)
#     return roll

# assert rollDice(0) == 0 
# assert rollDice(1000) != rollDice(1000) 
# for i in range(1000):
#     assert 1 <= rollDice(1) <= 6
#     assert 2 <= rollDice(2) <= 12
#     assert 3 <= rollDice(3) <= 18
#     assert 100 <= rollDice(100) <= 600

# My code:
one = """
-----
|   |
| o |
|   |
-----"""
two = """
-----
|o  |
|   |
|  o|
-----"""
three = """
-----
|o  |
| o |
|  o|
-----"""
four = """
-----
|o o|
|   |
|o o|
-----"""
five = """
-----
|o o|
| o |
|o o|
-----"""
six = """
-----
|o o|
|o o|
|o o|
-----"""

def rollDice(numberOfDice):
    result = ""
    for n in range(numberOfDice):
        roll = random.randint(1, 6)
        if roll == 1:
            result += one + " "
        elif roll == 2:
            result += two + " "
        elif roll == 3:
            result += three + " "
        elif roll == 4:
            result += four + " "
        elif roll == 5:
            result += five + " "
        elif roll == 6:
            result += six + " "
    return result

user = input("\nHow many dice are you rolling: ")
print(rollDice(int(user)))
sleep(50)