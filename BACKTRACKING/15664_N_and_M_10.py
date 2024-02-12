#-*- coding: utf-8 -*-

"""
N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성하시오. N개의 자연수는 모두 다른 수이다.
N개의 자연수 중에서 M개를 고른 수열
고른 수열은 비내림차순이어야 한다.
길이가 K인 수열 A가 A1 ≤ A2 ≤ ... ≤ AK-1 ≤ AK를 만족하면, 비내림차순이라고 한다.

4 2
9 7 9 1


import sys
import time
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))

start_time = time.time()
v = [0] * (N+1)
ans = set()

def dfs(n, lst):
    global ans
    if n == M:
        lst = tuple(lst)
        ans.add(lst)
        return
    for j in range(N):
        if v[j] == 0 and all([nums[j]>=x for x in lst]):
            v[j] = 1
            dfs(n+1, list(lst)+[nums[j]])
            v[j] = 0
            
dfs(0, ())
intermediate_time = time.time()
print(f"#1_time_elapsed : {intermediate_time - start_time}")

for lst in sorted(ans):
    print(*lst)
end_time = time.time()
print(f"#2_time elapsed : {end_time - start_time}")
"""

# 방법 1 : n은 선택할 숫자의 개수이고 j가 0부터 N-1까지 순회한다.
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
nums = list(map(int, input().split()))
ans = set()
v = [0] * N

def dfs(n, lst):
    global ans
    if n == M:
        ans.add(tuple(lst))
        return
    for j in range(N):
        if v[j] == 0 and all([nums[j] >= x for x in lst]):
            v[j] = 1
            dfs(n+1, lst+[nums[j]])
            v[j] = 0

dfs(0, [])
for lst in sorted(ans):
    print(*lst)
    
# 방법 2 : n은 선택한 숫자의 개수이고 j가 s+1부터 N-1까지 순회한다.