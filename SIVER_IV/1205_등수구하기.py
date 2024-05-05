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

from bisect import bisect_left, bisect_right

original_left_idx = bisect_left(sorted(lst), ts)
original_right_idx = bisect_right(sorted(lst), ts)

left_idx = len(lst) - original_right_idx
right_idx = len(lst) - original_left_idx

print(f"left_idx : {left_idx},  right_idx : {right_idx}")
