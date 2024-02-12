#-*- coding: utf-8 -*-
"""
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.
N개의 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.

4 2
9 7 9 1
"""

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
ans = set()

def dfs(n, lst):
    global ans
    if n == M:
        ans.add(tuple(lst))
        return
    for j in range(N):
        dfs(n+1, lst+[nums[j]])

dfs(0, [])
for lst in sorted(ans):
    print(*lst)