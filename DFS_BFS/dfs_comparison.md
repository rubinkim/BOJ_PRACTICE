```py
import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))
    
for row in graph:
    print(row)    
  
def dfs_deque(graph, start_x, start_y):
    if graph[start_x][start_y] == 1 and (start_x, start_y) not in path:
        q = deque([(start_x, start_y)])
        path.append((start_x, start_y))
        while q:
            x, y = q.pop()  
            if (x, y) not in path:
                path.append((x, y))    
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                        continue
                    if graph[nx][ny] == 1 and (nx, ny) not in path:
                        path.append((nx, ny))
                        q.append((nx, ny))
 

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
path = []
cnt = 0

for i in range(n):
    for j in range(n):
        if (i, j) not in path:
            if graph[i][j] == 1:
                dfs_deque(graph, i, j)
                cnt += 1
                print(f"{i, j} : {path}")
print(cnt)
```

