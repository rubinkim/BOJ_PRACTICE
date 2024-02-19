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
    
#print(lst)

for (x1, y1), (x2, y2) in combinations(lst, 2):
    if abs(x1 - x2) <= 10 and abs(y1 - y2) <= 10:
        if (x1 >= x2) and (y1 >= y2):
            overlapped += (x2 + 10 - x1) * (y2 + 10 - y1)
        elif (x1 >= x2) and (y1 < y2):
            overlapped += (x2 + 10 - x1) * (y1 + 10 - y2)
        elif (x1 < x2) and (y1 >= y2):
            overlapped += (x1 + 10 - x2) * (y2 + 10 - y1)
        elif (x1 < x2) and (y1 < y2):
            overlapped += (x1 + 10 - x2) * (y1 + 10 - y2)

print(N * 100 - overlapped)