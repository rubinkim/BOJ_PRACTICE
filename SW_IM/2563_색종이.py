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
for _ in range(N):
    lst.append(list(int, input().split()))
    
print(lst)
