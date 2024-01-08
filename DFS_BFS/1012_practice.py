#-*- coding: utf-8 -*-

"""
2
10 8 17
0 0
1 0
1 1
4 2
4 3
4 5
2 4
3 4
7 4
8 4
9 4
7 5
8 5
9 5
7 6
8 6
9 6
10 10 1
5 5

1
5 3 6
0 2
1 2
2 2
3 2
4 2
4 0
    
"""

def dfs(x,y):
    visited[x][y] = True
    directions = [ (-1, 0), (1, 0), (0, -1), (0, 1)]
    # 상하 좌우로 움직일 수 있는 방향을 지정해주고 여기서 for문을 돌린다.
    for dx, dy in directions:
        nx, ny = dx + x, dy+y
        if nx < 0 or nx >=n or ny<0 or ny>=m:
            continue
        if array[nx][ny] and not visited[nx][ny]:
            dfs(nx,ny)

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
                dfs(i,j)
                result += 1
    print(result)