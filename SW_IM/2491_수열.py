#-*- coding: utf-8 -*-
"""
9
1 2 2 4 4 5 7 7 2

9
4 1 3 3 2 2 9 2 3

11
1 5 3 6 4 7 1 3 2 9 5

(8   4   2)
"""

import sys
sys.setrecursionlimit(105000)
input = sys.stdin.readline
N = int(input())
nums = list(map(int, input().split()))
ans = [[0]]
max_len = 1

def dfs(n, lst_asc, lst_desc):      # n : nums라는 list의 각 원소들의 index
    global ans, max_len
    max_len = max([len(x) for x in ans])
    if n >= N:
        if len(lst_asc) > max_len:
            ans.append(lst_asc)
        if len(lst_desc) > max_len:
            ans.append(lst_desc)
        return
    elif n < N:
        if nums[n] > nums[n-1]:
            if len(lst_desc) > max_len:
                ans.append(lst_desc)
            lst_desc = [nums[n]]
            dfs(n+1, lst_asc+[nums[n]], lst_desc)
    
        elif nums[n] == nums[n-1]:
            if len(lst_asc) > max_len:
                ans.append(lst_asc)
            if len(lst_desc) > max_len:
                ans.append(lst_desc)
            dfs(n+1, lst_asc+[nums[n]], lst_desc+[nums[n]])
        
        elif nums[n] < nums[n-1]:
            if len(lst_asc) > max_len:
                ans.append(lst_asc)
            lst_asc = [nums[n]]
            dfs(n+1, lst_asc, lst_desc+[nums[n]])
        
dfs(1, [nums[0]], [nums[0]])
print(max_len)