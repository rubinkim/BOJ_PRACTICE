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
    row = map(int, input().split())
    for j in range(m):
        arr[i][j] = row[j]

for row in arr:
    print(row)