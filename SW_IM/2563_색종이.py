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
    if abs(area0[0] - area1[0]) < 10 and  abs(area0[1] - area1[1]) < 10:
        if area0[0] <= area1[0] and area0[1] <= area1[1]:
            overlapped += abs(area0[0]+10 - area1[0]) * abs(area0[1]+10 - area1[1])
        elif area0[0] > area1[0] and area0[1] <= area1[1]:
            overlapped += abs(area1[0]+10 - area0[0]) * abs(area0[1]+10 - area1[1])
        elif area0[0] <= area1[0] and area0[1] > area1[1]:
            overlapped += abs(area0[0]+10 - area1[0]) * abs(area1[1]+10 - area0[1])
        elif area0[0] > area1[0] and area0[1] > area1[1]:
            overlapped += abs(area1[0]+10 - area0[0]) * abs(area1[1]+10 - area0[1])

print(overlapped)
