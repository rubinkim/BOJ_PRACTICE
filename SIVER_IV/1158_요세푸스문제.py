#-*- coding: utf-8 -*-
"""
7 3

(<3, 6, 2, 7, 5, 1, 4>)
"""

n, k = map(int, input().split())
lst = list(range(1, n+1))
print(f"n : {n},  k : {k},  lst : {lst}")

ans = []
cnt = 0
while True:
    if len(lst) == 1:
        ans.append(lst.pop())
        break
    if len(lst) >= k:
        ans.append(lst.pop(k-1))
        cnt += 1
        lst = lst[k-1:] + lst
        lst = lst[:n-cnt]
    elif len(lst) < k:
        lst += lst
        ans.append(lst.pop(k-1))
        cnt += 1
        lst = lst[k-1:] + lst
        lst = lst[:n-cnt]
        
print(ans)
print(f"<{ans}>")