#-*- coding: utf-8 -*-
"""
9
1 2 2 4 4 5 7 7 2

9
4 1 3 3 2 2 9 2 3

11
1 5 3 6 4 7 1 3 2 9 5

(8   4   2)


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
"""
"""
n개의 수가 나열된 수열이 있다. 그 수열 안에서 연속해서 커지거나 작아지는 수열 중 가장 길이가 긴 것을 찾아, 
그 길이를 출력하는 문제. 커지는 것과 작아지는 것을 관리하는 두 배열을 만든 후 반복문을 이용하여 조건에 충족했을 때 
dp[i] = dp[i-1] + 1의 점화식을 이용하여 풀었다.
"""
n = int(input())
lst = list(map(int, input().split()))
pdp = [1 for _ in range(n)]
ndp = [1 for _ in range(n)]

for i in range(1, n):
    if lst[i] >= lst[i-1]: 
        pdp[i] = pdp[i-1] + 1
    if lst[i] <= lst[i-1]: 
        ndp[i] = ndp[i-1] + 1

print(max(max(pdp), max(ndp)))