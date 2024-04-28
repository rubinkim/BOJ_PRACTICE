#-*- coding: utf-8 -*-
"""
7
(1 3 5 7 4 2 6)

# Using queue
from collections import deque
n = int(input())
arr = list(range(1, n+1))
arr = deque(arr)
#print(arr)
lst = []

while len(arr) >= 2:
    lst.append(arr.popleft())
    if len(arr) >= 2:
        arr.append(arr.popleft())
    else:
        break

if len(lst):   
    print(*lst, end=' ')
    print(arr[0])
else:
    print(arr[0])
"""

# Using stack
n = int(input())
arr = list(range(1, n+1))
lst = []

while len(arr) >= 2:
    lst.append(arr.pop(0))
    if len(arr) >= 2:
        arr.append(arr.pop(0))
    else:
        break

if len(lst):
    print(*lst, end=' ')
    print(arr[0])
else:
    print(arr[0])

