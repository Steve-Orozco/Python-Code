#!/usr/bin/python3.10
######## 1
"""
def EvenNums(num):
    print(num)
    if num % 2 != 0:
        print("Please enter an even number!")
    elif num == 2:
        return num
    else:
        return EvenNums(num-2)


print(EvenNums(200))

####### 2
"""
# A sequence where the next value equals the sum of its 2 previous values 
import time
def fibonacci(index_of_Number): # Iteration 
   seq = [0, 1]
   for i in range(index_of_Number):
      seq.append(seq[-1]+seq[-2])
   return seq[-2]

def Fibonacci(index_of_Number): # Recursion
    if index_of_Number <= 1:
        return index_of_Number
    else:
        return Fibonacci(index_of_Number-1)+Fibonacci(index_of_Number-2)

t1 = time.perf_counter()
t2 = time.perf_counter()
print(f'fibonacci(8){t1}')
print(f'Fibonacci(8){t2}')



######### 3


