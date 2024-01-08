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

from collections import deque

def connected_component_mutant(graph, start_y, start_x, num):    
    dy = [0, 0, -1, 1]
    dx = [-1, 1, 0, 0]    
    
    q = deque()
    
    if start_y <= -1 or start_y >= n or start_x <= -1 or start_x >= m:
        return False    
    if graph[start_y][start_x] == 1 and not visited[start_y][start_x]:
        q.append((start_y, start_x))
        visited[start_y][start_x] = True
        
        while q:
            y, x = q.pop()                     # x, y = q.popleft()로 하면 bfs이다.
            cnt = 0
            
            for i in range(4):                
                ny = y + dy[i]
                nx = x + dx[i]
                
                if ny <= -1 or ny >= n or nx <= -1 or nx >= m:
                    continue
                if graph[ny][nx] == 1 and not visited[ny][nx]:
                    q.append((ny, nx))
                    visited[ny][nx] = True                    
                    cnt += 1                           
        return True
    return False

num_usecases = int(input())

for i in range(num_usecases):    
    m, n, k = map(int, input().split())    
    graph = [[0] * m for _ in range(n)]
    visited = [[False]*m for _ in range(n)]
    for _ in range(k):
        x, y = map(int, input().split())        
        graph[y][x] = 1       
        
    ans = 1
    for i in range(n):
        for j in range(m):
            if connected_component_mutant(graph, i, j, ans) == True:
                ans += 1  

    print(ans - 1)
    
    