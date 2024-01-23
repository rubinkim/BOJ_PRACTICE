#-*- coding: utf-8 -*-
"""
4 2
"""

n, m = map(int, input().split())
ans = []

def back(start, end):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
    for i in range(start, end):
        if i not in ans:
            ans.append(i)
            back(start+1, end)
            ans.pop()
            
back(1, n+1)