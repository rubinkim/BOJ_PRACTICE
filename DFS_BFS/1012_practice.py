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

from collections import deque
path = []
num_dict = {}

def connected_component_mutant(graph, start_y, start_x, num):
    global path, num_dict
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]    
    
    q = deque()
    
    if start_y <= -1 or start_y >= n or start_x <= -1 or start_x >= m:
        return False    
    if graph[start_y][start_x] == 1 and (start_y, start_x) not in path:
        q.append((start_y, start_x))
        path.append((start_y, start_x))
        graph[start_y][start_x] = num
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
        
        while q:
            y, x = q.pop()                     # x, y = q.popleft()로 하면 bfs이다.
            cnt = 0
            
            for i in range(4):                
                ny = y + dy[i]
                nx = x + dx[i]
                
                if ny <= -1 or ny >= n or nx <= -1 or nx >= m:
                    continue
                if graph[ny][nx] == 1 and (ny, nx) not in path:
                    q.append((ny, nx))
                    path.append((ny, nx))
                    graph[ny][nx] = num
                    cnt += 1
                    num_dict[num] += 1        
        return True
    return False

num_usecases = int(input())

for i in range(num_usecases):    
    m, n, k = map(int, input().split())    
    graph = [[0] * m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())        
        graph[y][x] = 1       
        
    ans = 1
    for i in range(n):
        for j in range(m):
            if connected_component_mutant(graph, i, j, ans) == True:
                ans += 1  

    print(ans - 1)