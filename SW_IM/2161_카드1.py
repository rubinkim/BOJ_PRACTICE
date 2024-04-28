#-*- coding: utf-8 -*-
"""
7
(1 3 5 7 4 2 6)
"""
from collections import deque
n = int(input())
arr = list(range(1, n+1))
arr = deque(arr)
print(arr)
lst = []

while len(arr) >= 2:
    arr.popleft()
    if len(arr) >= 2:
        lst.append(arr.popleft())

