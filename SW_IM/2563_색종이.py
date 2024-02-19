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

for area0, area1 in combinations(lst, 2):


print(3 * 100 - overlapped)
