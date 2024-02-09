#-*- coding: utf-8 -*-
"""
4 2
"""
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
            
back()
"""
"""
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ans = []

def dfs(n, lst):
    global ans    

    if n > N:
        if len(lst) == M:
            ans.append(lst)
        return
    dfs(n+1, lst+[n])
    dfs(n+1, lst)

dfs(1, [])
for lst in ans:
    print(*lst)
"""

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ans = []
v = [0] * (N+1)

def dfs(n, lst):
    global ans
    if n == M:
        ans.append(lst)
        return
    for j in range(1, N+1):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, lst+[j])
            v[j] = 0

dfs(0, [])
for lst in ans:
    print(*lst)
   
"""
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ans = []

def dfs(n, s, lst):
    if n == M:
        ans.append(lst)
        return
    for j in range(s, N+1):
        dfs(n+1, j+1, lst+[j])
        
dfs(0, 1, [])
for lst in ans:
    print(*lst)
"""