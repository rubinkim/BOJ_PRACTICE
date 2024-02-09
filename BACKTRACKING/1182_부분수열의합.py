#-*- coding: utf-8 -*-

"""
5 0
-7 -3 -2 5 8

7 0
9 1 -7 -3 -2 5 8 

5 6
1 2 3 4 5
"""

import sys
input = sys.stdin.readline
N, S = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0

def dfs(n, sm, cnt):
    global ans
    #종료조건
    if n == N:
        if sm == S and cnt > 0:
            ans += 1
        return
    #하부함수 호출
    dfs(n+1, sm+lst[n], cnt+1)  #lst[n]을 포함시키는 경우
    dfs(n+1, sm, cnt)           #lst[n]을 포함시키지 않는 경우

dfs(0, 0, 0)
print(ans)