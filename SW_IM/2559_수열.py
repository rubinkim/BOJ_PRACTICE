#-*- coding: utf-8 -*-
"""
10 2
3 -2 -4 -9 0 3 7 13 8 -3

21


10 5
3 -2 -4 -9 0 3 7 13 8 -3

31

N, K = map(int, input().split())
lst = list(map(int, input().split()))

max_val = -1001
for i in range(len(lst) - K + 1):
    max_val = max(max_val, sum([x for x in lst[i:i+K]]))
print(max_val)
"""

N, K = map(int, input().split())
lst = list(map(int, input().split()))

max_val = -1001
for i in range(len(lst) - K + 1):
    if i == 0:
        max_val = max(max_val, sum([x for x in lst[i:i+K]]))
    else:
        max_val = max(max_val, max_val - lst[i-1] + lst[i+K])
print(max_val)