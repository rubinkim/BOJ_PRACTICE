#-*- coding: utf-8 -*-
"""
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.
N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

4 2
9 8 7 1

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
ans = []

def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return
    for j in range(N):
        if all([nums[j] >= x for x in lst]):
            dfs(n+1, lst+[nums[j]])
            
dfs(0, [])
for lst in sorted(ans):
    print(*lst)
"""

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
ans = []

def dfs(n, lst):
    global ans
    if n == M:
        ans.append(lst)
        return
    for j in range(N):
        if all([nums[j] >= x for x in lst]):
            dfs(n+1, lst+[nums[j]])

dfs(0, [])
for lst in ans:
    print(*lst)