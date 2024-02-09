#-*- coding: utf-8 -*-
"""
4 2
"""
"""
# 나의 저급한 방법
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

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ans = []

def dfs(n, lst):
    global ans    
    # 종료조건
    if n > N:
        if len(lst) == M:
            ans.append(lst)
        return
    dfs(n+1, lst+[n])
    dfs(n+1, lst)

dfs(1, [])
for lst in ans:
    print(*lst)