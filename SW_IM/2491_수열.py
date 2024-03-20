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

N = int(input())
nums = list(map(int, input().split()))
print(f"N : {N},  nums : {nums}")

print()
ans = []

def dfs(n, lst_asc, lst_desc):      # n : nums라는 list의 각 원소들의 index
    if n >= N:
        lens_lst = [len(x) for x in ans]
        return max(lens_lst)
    
    if nums[n] >= nums[n-1]:
        ans.append(lst_desc)
        lst_desc = []
        dfs(n+1, lst_asc+[nums[n]], lst_desc)
        
    if nums[n] <= nums[n-1]:
        ans.append(lst_asc)
        lst_asc = []
        dfs(n+1, lst_asc, lst_desc+[nums[n]])
print(dfs(1, [nums[0]], [nums[0]]))