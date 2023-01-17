#!/usr/bin/python3.10

"""
Converts Celsius to Fahrenheit
"""

print("Input degree for conversion: ")
cel = int(input())

def conv(n):
   return 9/5 * n + 32 # Formula for conversion, found on google.
    

fah = conv(cel)
print(f'From {cel}° celsius to {fah}° fahrenheit')