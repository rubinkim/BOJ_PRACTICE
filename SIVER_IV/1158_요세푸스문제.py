#-*- coding: utf-8 -*-
"""
7 3

(<3, 6, 2, 7, 5, 1, 4>)
"""

n, k = map(int, input().split())
lst = list(range(1, n+1))
print(f"n : {n},  k : {k},  lst : {lst}")

ans = []
while True:
    if len(lst) == 1:
        break
    if len(lst) >= k:
        ans.append(lst.pop(k-1))
    elif len(lst) < k:
        lst += lst
        ans.append(lst.pop(k-1))
        
print(ans)