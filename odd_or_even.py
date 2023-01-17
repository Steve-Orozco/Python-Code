#!/usr/bin/python3.10
"""
# Selects number from random
from random import randint
number = randint(1, 1000)

if (number % 2) == 0:
    print("Is Even")
else:
    print("Is Odd")
"""
# Selects Number from input
inputs = int(input("Please enter a number: "))

if (inputs % 2) == 0:
    print("Is Even")
else:
    print("Is Odd")
exit
