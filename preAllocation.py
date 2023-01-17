#!/usr/bin/python3.10
import time
# Dynamic Storage

start = time.time()
list = []
for num in range(30_000_000):
   list.append(num)
end = time.time()
print(f'Dynamic Storage\nSeconds: {end-start}\n\n')

# Pre-Allocation
start = time.time()
list2 = [0]*30_000_000
for num in range(30_000_000):
   list2[num] = num
end = time.time()
print(f'Pre-Allocation\nSeconds: {end-start}')