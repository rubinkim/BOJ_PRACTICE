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
import sys
sys.setrecursionlimit(1000)

n, m = map(int, input().split())    # n : number of columns,  m : number of rows
arr = [[0] * n for _ in range(m)]
current = 0

def dfs(y, x):
    global current
    
    dy = [0, -1, 0, 1]
    dx = [1, 0, -1, 0]    
    
    arr[y][x] = 1
    ny, nx = y + dy[current], x + dx[current]
    
    if (0 <= ny <= m-1) and (0 <= nx <= n-1) and arr[ny][nx] == 0:
        y, x = ny, nx
        dfs(y, x)
    else:
        current = (current + 1) % 4
        ny, nx = y + dy[current], x + dx[current]
        if (0 <= ny <= m-1) and (0 <= nx <= n-1) and arr[ny][nx] == 0:
            y, x = ny, nx
            dfs(y, x)
        else:
            print(x, m-1-y)
            exit(0)            
        
dfs(3, 0)
