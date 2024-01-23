#-*- coding: utf-8 -*-
"""
4 2
"""

n, m = map(int, input().split())
ans = []

def back(start):
    if len(ans) == m:
        print(" ".join(map(str, ans)))
    for i in range(start, n+1):
        if i not in ans:
            ans.append(i)
            back(start+1)
            ans.pop()
            
            
back(1)