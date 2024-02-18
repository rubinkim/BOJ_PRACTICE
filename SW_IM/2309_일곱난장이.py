#-*- coding: utf-8 -*-

"""
20
7
23
19
10
15
25
8
13
"""
from itertools import combinations
import sys

input = sys.stdin.readline
lst = []
for _ in range(9):
    lst.append(int(input()))
    
#print(lst)

for x in combinations(lst, 7):
    if sum(x) == 100:
        x = list(x)
        x.sort()
        ans = x
        break
    
for i in ans:
    print(i)