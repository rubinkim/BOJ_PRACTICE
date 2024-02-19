#-*- coding: utf-8 -*-

"""
3
3 7
15 7
5 2

260
"""

from itertools import combinations
import sys
input = sys.stdin.readline
N = int(input())
lst = []
overlapped = 0

for _ in range(N):
    lst.append(list(map(int, input().split())))
    
print(lst)

for (x1, y1), (x2, y2) in combinations(lst, 2):
    if (x1 >= x2) and ()

print(3 * 100 - overlapped)
