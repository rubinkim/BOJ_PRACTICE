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
    
lo, hi = 1, min(n, m)
mid = (lo + hi) // 2
ans = 1

while lo <= hi:
    for i in range(n-mid):
        for j in range(m-mid):
            area_sum = sum([sum([arr[ii][jj] for jj in range(j, j+mid)]) for ii in range(i, i+mid)])
            print(f"(i, j) {i, j},  area_sum : {area_sum}")
            ans = max(ans, area_sum)
    if area_sum == mid ** 2:
        ans = max(ans, area_sum)
        lo = mid + 1
    elif area_sum < mid ** 2:
        hi = mid - 1
    mid = (lo + hi) // 2
                

print(ans)