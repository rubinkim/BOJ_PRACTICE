#-*- coding: utf-8 -*-
"""
4 4
0100
0111
1110
0010

(4)


n, m = map(int, input().split())
arr = [[] for _ in range(n)]
for i in range(n):
    row = list(map(int, input()))
    for j in range(m):
        arr[i].append(row[j])  
        
for row in arr:
    print(row)   
        
dp = [[0] * m for _ in range(n)]
ans = 0

for j in range(m):
    if arr[0][j] == 1:
        dp[0][j] = 1

for i in range(1, n):
    if arr[i][0] == 1:
        dp[i][0] = 1
    for j in range(1, m):
        if arr[i][j] == 1:
            dp[i][j] = min(dp[i][j-1], dp[i-1][j], dp[i-1][j-1]) + 1

for i in range(n):
    for j in range(m):
        ans = max(ans, dp[i][j])

print(ans**2)
"""
n, m = map(int, input().split())
arr = [[] for _ in range(n)]
for i in range(n):
    row = list(map(int, input()))
    for j in range(m):
        arr[i].append(row[j])  
        
for row in arr:
    print(row) 