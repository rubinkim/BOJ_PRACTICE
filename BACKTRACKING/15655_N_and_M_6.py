#-*- coding: utf-8 -*-

"""
4 2
9 8 7 1
"""

N, M = map(int, input().split())
nums = list(map(int, input().split()))

ans = []
v = [0] * (N+1)

def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return
    for j in range(1, N+1):
        if v[j] == 0 and all([nums[j] >= x for x in lst]):
            v[j] = 1
            dfs(n+1, lst+[nums[j]])
            v[j] = 0

dfs(0, [])
for lst in ans:
    print(*lst)