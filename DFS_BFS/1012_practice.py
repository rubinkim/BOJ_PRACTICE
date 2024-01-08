#-*- coding: utf-8 -*-

"""

1
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0
    
"""
"""
from collections import deque

def bfs(x,y):
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    while q:
        x, y = q.popleft()
        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            if array[nx][ny] and not visited[nx][ny]:
                q.append((nx,ny))
                visited[nx][ny]=True


for _ in range(int(input())):
    m, n, k = map(int,input().split())
    array=[[0]*m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    for _ in range(k):
        y, x = map(int,input().split())
        array[x][y] = 1
    result = 0
    for i in range(n):
        for j in range(m):
            if array[i][j] and not visited[i][j]:
                bfs(i,j)
                result += 1
    print(result)
"""   

