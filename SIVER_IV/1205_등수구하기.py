#-*- coding: utf-8 -*-
"""
3 90 10
100 90 80
(2)

10 1 10
10 9 8 7 6 5 4 3 2 1
(-1)

10 1 10
10 9 8 7 6 5 4 3 3 0
(10)

0 0 50
(1)
"""

n, ts, p = map(int, input().split())
lst = list(map(int, input().split()))
print(f"n : {n},  ts : {ts},  p : {p}")
print(f"lst : {lst}")