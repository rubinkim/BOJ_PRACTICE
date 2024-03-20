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
#print(f"N : {N},  nums : {nums}")

#print()
ans = []

def dfs(n, lst_asc, lst_desc):      # n : nums라는 list의 각 원소들의 index
    global ans
    if n >= N:
        ans.append(lst_asc)
        ans.append(lst_desc)
        return
    
    if nums[n] > nums[n-1]:
        ans.append(lst_desc)
        lst_desc = [nums[n]]
        dfs(n+1, lst_asc+[nums[n]], lst_desc)
    
    elif nums[n] == nums[n-1]:
        dfs(n+1, lst_asc+[nums[n]], lst_desc+[nums[n]])
        
    elif nums[n] < nums[n-1]:
        ans.append(lst_asc)
        lst_asc = [nums[n]]
        dfs(n+1, lst_asc, lst_desc+[nums[n]])
        
dfs(1, [nums[0]], [nums[0]])
max_len = 0
for x in ans:
    if len(x) > max_len:
        max_len = len(x)
print(max_len)

"""
N = int(input())
nums = list(map(int, input().split()))
#print(f"N : {N},  nums : {nums}")

ans = []
lst_asc,  lst_desc = [nums[0]], [nums[0]]

for i in range(1, N+1):
    if nums[i] > nums[i-1]:
        lst_asc.append(nums[i])
        lst_desc = []
    elif nums[i] == nums[i-1]:
        lst_asc.append(nums[i])
        lst_desc.append(nums[i])
    elif nums[i] < nums[i-1]:
        lst_asc = []
        lst_desc.append(nums[i])
"""