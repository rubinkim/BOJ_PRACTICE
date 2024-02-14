#-*- coding: utf-8 -*-
"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10

10
5 10
5 9
5 8
5 7
5 6
5 10
5 9
5 8
5 7
5 6

10
5 50
4 40
3 30
2 20
1 10
1 10
2 20
3 30
4 40
5 50
"""
import sys
input = sys.stdin.readline
N = int(input())
T, P = [0] * N,  [0] * N
for i in range(N):
    T[i], P[i] = map(int, input().split())
    
ans = 0 

def dfs(n, sm):
    if n >= N:
        ans = max(ans, sm)
    
    if n + T[n] <= N:
        dfs(n+T[n], sm+P[n])
    dfs(n+1, sm)

dfs(0, 0)
print(ans)



    