#-*- coding: utf-8 -*-
"""
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. (1 ≤ M ≤ N ≤ 7)
1부터 N까지 자연수 중에서 M개를 고른 수열
같은 수를 여러 번 골라도 된다.
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.
수열은 사전 순으로 증가하는 순서로 출력해야 한다.
"""

import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ans = []

def dfs(n, lst):
    if n == M:
        ans.append(lst)
        return
    for j in range(1, N+1):
        if all([j >= x for x in lst]):
            dfs(n+1, lst+[j])

dfs(0, [])
for lst in ans:
    print(*lst)