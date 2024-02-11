#-*- coding: utf-8 -*-

"""
4 2
9 8 7 1
"""

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
v = [0] * N
ans = []

def dfs(n, lst):
    global ans
    if n == M:
        ans.append(lst)
        return
    for j in range(N):
        if v[j] == 0 and all([nums[j]>x for x in lst]):
            v[j] = 1
            dfs(n+1, lst+[nums[j]])
            v[j] = 0

dfs(0, [])
for lst in ans:
    print(*lst)
    
    
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
v = [0] * N
ans = []

def dfs(n, s, lst):
    global ans
    if n == M:
        ans.append(lst)
        return
    for j in range(s, N):
        if v[j] == 0 and all([nums[j]>x for x in lst]):
            v[j] = 1
            dfs(n+1, j+1, lst+[nums[j]])
            v[j] = 0

dfs(0, 0, [])
for lst in ans:
    print(*lst)
    
    
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []

def dfs(n, num_lst, lst):
    global ans
    if n > N-1:
        if len(lst) == M:
            ans.append(lst)
        return
    dfs(n+1, num_lst, lst+[nums[n]])
    dfs(n+1, num_lst, lst)

dfs(0, nums, [])
for lst in ans:
    print(*lst)