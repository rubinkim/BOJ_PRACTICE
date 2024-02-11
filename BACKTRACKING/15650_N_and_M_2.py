#-*- coding: utf-8 -*-
"""
4 2
"""
"""
# 방법 1 : n = 선택한 숫자의 개수이고, j가 1부터 N까지 반복하는데 j가 lst에 이미 있는 다른 값들보다 커야 한다는 조건을 추가한다.
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ans = []
v = [0] * (N+1)

def dfs(n, lst):
    global ans
    if n == M:
        ans.append(lst)
        return
    for j in range(1, N+1):
        if v[j] == 0 and all([j > x for x in lst]):
            v[j] = 1
            dfs(n+1, lst+[j])
            v[j] = 0
dfs(0, [])
for lst in ans:
    print(*lst)

# 방법 2 : n = 선택한 숫자의 개숫이고 j가 바로 전 단계에서 선택한 숫자보다 하나 큰 숫자부터 N까지 반복하도록 s라는 변수를 이용했다.
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ans = []
v = [0] * (N+1)

def dfs(n, s, lst):
    global ans
    if n == M:
        ans.append(lst)
        return
    for j in range(s, N+1):
        if v[j] == 0:
            v[j] = 1
            dfs(n+1, j+1, lst+[j])
            v[j] = 0

dfs(0, 1, [])
for lst in ans:
    print(*lst)
"""   
    
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
ans = []

def dfs(n, lst):
    global ans
    if n > N:
        if len(lst) == M:
            ans.append(lst)
        return
    dfs(n+1, lst+[n])
    dfs(n+1, lst)

dfs(1, [])
for lst in ans:
    print(*lst)