#-*- coding: utf-8 -*-
"""
4 2
"""

n, m = map(int, input().split())
ans = []

def back():
    if len(ans) == m:
        print(" ".join(map(str, ans)))
    for i in range(1, n+1):
        if i not in ans and all(i - x > 0 for x in ans):
            ans.append(i)
            back()
            ans.pop()
            
            
back(1)