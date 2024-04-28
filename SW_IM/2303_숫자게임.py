#-*- coding: utf-8 -*-
"""
3
7 5 5 4 9
1 1 1 1 1
2 3 3 2 10

(1)
"""
from itertools import combinations
n = int(input())
lst = []

for _ in range(n):
    max_first_digit = -1