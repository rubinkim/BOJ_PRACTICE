#-*- coding: utf-8 -*-
"""
6 4
(1 2)

6 5
(3 2)

1 11
(0 10)

12 50
(5 6)

(5000 5000)
2499 2500
"""

n, m = map(int, input().split())    # n : number of columns,  m : number of rows
arr = [[0] * n for _ in range(m)]
dy = [0, -1, 0, 1]
dx = [1, 0, -1, 0]
current = 0

for i in range(m):
    for j in range(n):
        y, x = m-1-i, j
        arr[y][x] = 1
        ny, nx = y+dy[current], x+dx[current]
        
        if (0 <= ny <= m-1) and (0 <= nx <= n-1) and arr[ny][nx] == 0:
            y, x = ny, nx
        
        