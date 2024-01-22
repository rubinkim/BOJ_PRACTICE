#-*- coding: utf-8 -*-

"""
3  6  10
 
2 4
CAAB
ADCB

3 6
HFDFFB
AJHGDH
DGAGEH

5 5
IEFCJ
FHFKC
FFALF
HFGCF
HMCHH
"""

import sys
input = sys.stdin.readline

r, c = map(int, input().rstrip().split())
graph = []
for _ in range(r):    
    graph.append(list(input()))
path = []
max_length = 0

def dfs_recursion(start_x, start_y, depth):
    global max_length
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    path.append(graph[start_x][start_y])        
    max_length = max(max_length, len(path))
    
    for i in range(4):
        nx, ny = start_x + dx[i], start_y + dy[i]
        if nx <= -1 or nx >= r or ny <= -1 or ny >= c:
            continue
        if graph[nx][ny] not in path:
            dfs_recursion(nx, ny, depth+1)            
            path.pop()
            
dfs_recursion(0, 0, 0)
print(max_length)   


































"""
total_path = []    
cnt = 0

def logest_path(graph, start_x, start_y):
    global cnt, total_path
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    path = []
    visited = [[False] * c for _ in range(r)]
    if start_x <= -1 or start_x >= r or start_y <= -1 or start_y >= c:
        return False
    if graph[start_x][start_y] not in path and not visited[start_x][start_y]:        
        q = deque()
        q.append((start_x, start_y))
        path.append(graph[start_x][start_y])
        visited[start_x][start_y] = True
        cnt += 1

        while q:
            x, y = q.popleft()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx <= -1 or nx >= r or ny <= -1 or ny >= c:
                    continue
                if graph[nx][ny] not in path and not visited[nx][ny]:
                    sub_dict = {}
                    sub_path = []
                    sub_dict[i] = graph[nx][ny]                    
                    path.append(sub_dict[i])
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
                print(f"i : {i}, (x,y) : {(x,y)} sub_dict : {sub_dict}")
                print()
                total_path.append(path)
                print(f"total_path : {total_path}")

        return True
    return False

logest_path(graph, 0, 0)
print(f"path : {total_path}")
print(f"cnt : {cnt}")
"""          
