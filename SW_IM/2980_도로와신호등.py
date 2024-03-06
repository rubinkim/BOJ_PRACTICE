#-*- coding: utf-8 -*-
"""
2 10
3 5 5
5 2 2

12

4 30
7 13 5
14 4 4
15 3 10
25 1 1

36
"""

N, L = map(int, input().split())
drg = [(0, 0, 0)]
for _ in range(N):
    d, r, g = map(int, input().split())
    drg.append((d, r, g))