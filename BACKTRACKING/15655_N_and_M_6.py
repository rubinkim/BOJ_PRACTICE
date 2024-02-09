#-*- coding: utf-8 -*-

"""
4 2
9 8 7 1
"""

import sys
input = sys.stdin.readline
N, M = map(int, input().split()) 
nums = list(map(int, input().split()))    
ans = []

def dfs(n, lst):
    global ans
    v = [0] * (N+1)
    if n == M:
        ans.append(lst)
        return
    for j in range(N):
            
        if v[j] == 0 and all([nums[j] > x for x in lst]): 
            v[j] = 1
            dfs(n+1, lst + [nums[j]])
            v[j] = 0

dfs(0, [])
for lst in sorted(ans):
    print(*lst)