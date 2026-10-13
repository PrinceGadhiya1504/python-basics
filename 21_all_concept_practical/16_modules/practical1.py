# Ek Python program banao jo:
# 1. math module import karke kisi number ka square root nikale.
# 2. math ke ceil() aur floor() se decimal number ko round up aur round down kare.
# 3. from math import pi se pi import kare aur circle ka area calculate kare.
# 4. random module ko rand alias se import kare aur randint() se 1–10 ke beech random number generate kare.
# 5. datetime module ko dt alias se import karke current date nikale.
# 6. Saare results clearly print kare.

# Expected checks:
# - Square root: 5.0
# - ceil(7.6): 8
# - floor(7.6): 7
# - Circle area: lagbhag 78.54
# - Random number: 1 se 10 ke beech koi bhi integer
# - Current date: program run karne ki date

import math
import random as rand
import datetime as dt

square = math.sqrt(25)
ceil = math.ceil(7.6)
floor = math.floor(7.6)
area = math.pi * 5 ** 2
random = rand.randint(1,10)
date = dt.datetime.now().date()

print(f"Square root of 25: {square}")
print(f"Ceil of 7.6: {ceil}")
print(f"Floor of 7.6: {floor}")
print(f"Area of circle with radius 5: {area}")
print(f"Random number between 1 and 10: {random}")
print(f"Current date: {date}")