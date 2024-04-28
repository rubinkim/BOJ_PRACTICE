#-*- coding: utf-8 -*-
"""
2 3
1 2 4
8 16 32
3
1 1 2 3
1 2 1 2
1 3 2 3

(63
2
36)
"""

n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
for i in range(n):
    row = list(map(int, input().split()))
    for j in range(m):
        arr[i][j] = row[j]

for row in arr:
    print(row)
    
k = int(input())
for _ in range(k):
    x1, y1, x2, y2 = map(int, input().split())
    ans = sum([sum([arr[i][j] for j in range(y1-1, y2)]) for i in range(x1-1, x2)])