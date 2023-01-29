# Exercise #19: Password Generator
import random

LOWER_LETTERS = "abcdefghijklmnopqrstuvwxyz"
UPPER_LETTERS = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
NUMBERS = "1234567890"
SPECIAL = "~!@#$%^&*()_+"
COMBINED = LOWER_LETTERS+UPPER_LETTERS+NUMBERS+SPECIAL

def generatePassword(length):
    password = []
    if length < 12:
        length = 12
    password += random.choice(LOWER_LETTERS), random.choice(UPPER_LETTERS), random.choice(NUMBERS), random.choice(SPECIAL)
    for x in range(length-4):
        password += random.choice(COMBINED)
    random.shuffle(password)
    return "".join(x for x in password)

len(generatePassword(8)) == 12
pw = generatePassword(14) 
assert len(pw) == 14 
hasLowercase = False 
hasUppercase = False 
hasNumber = False 
hasSpecial = False 
for character in pw:
    if character in LOWER_LETTERS: 
        hasLowercase = True
    if character in UPPER_LETTERS:
        hasUppercase = True
    if character in NUMBERS:
        hasNumber = True 
    if character in SPECIAL:
        hasSpecial = True 
assert hasLowercase and hasUppercase and hasNumber and hasSpecial
