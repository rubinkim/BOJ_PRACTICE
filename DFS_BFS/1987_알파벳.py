#-*- coding: utf-8 -*-

"""
 시간 제한	    메모리 제한	    제출	 정답	  맞힌 사람	      정답 비율
  2초	       256 MB	    112859	 33642	   20494	      28.281%

답안 : 3  6  10
 
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

from collections import deque

r, c = map(int, input().split())
graph = [[0] * c for _ in range(r)]
for i in range(r):    
    for j, x in enumerate(input()):
        graph[i][j] = x

for row in graph:
    print(row)
print()
    
visited = [[False] * c for _ in range(r)]
path = []
cnt = 0

def logest_path(graph, start_x, start_y):
    global visited, path, cnt
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    if start_x <= -1 or start_x >= r or start_y <= -1 or start_y >= c:
        return False
    if graph[start_x][start_y] not in path and not visited[start_x][start_y]:
        q = deque()
        q.append((start_x, start_y))
        path.append(graph[start_x][start_y])
        visited[start_x][start_y] = True
        cnt += 1        

        x, y = q.pop()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx <= -1 or nx >= r or ny <= -1 or ny >= c:
                continue
            if graph[nx][ny] not in path and not visited[nx][ny]:
                q.append((nx, ny))
                path.append(graph[nx][ny])
                visited[nx][ny] = True
                cnt += 1
        return True
    return False

logest_path(graph, 0, 0)
print(path)
print(cnt)
          
