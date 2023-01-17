#!/usr/bin/python3.10

nums = range(0, 1001)
def is_prime(num):
    for x in range(2,num):
       if (num % x) == 0:
          return False
       return True

def is_even(num):
   for i in range(2, num):
      if (num % i) != 0:
         return False
      return True
   

primes = list(filter(is_prime, nums))
print(primes,"\n\n")

even = list(filter(is_even, nums))
print(even)