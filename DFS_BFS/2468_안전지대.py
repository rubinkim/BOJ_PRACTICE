#-*- coding: utf-8 -*-
"""
5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

7
9 9 9 9 9 9 9
9 2 1 2 1 2 9
9 1 8 7 8 1 9
9 2 7 9 7 2 9
9 1 8 7 8 1 9
9 2 1 2 1 2 9
9 9 9 9 9 9 9

정답은 (5, 6)
"""

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))
    
min_graph = [[graph[j] for j in range(len(graph[i]))] for i in range(len(graph))]
print(f"min_graph : {min_graph}")

path = []
cc_num_list = []
cnt = 0
    
def dfs(graph, start_x, start_y, height):
    global path, cnt
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    
    if start_x <= -1 or start_x >= n or start_y <= -1 or start_y >= n:
        return False
    if graph[start_x][start_y] > height and (start_x, start_y) not in path:
        q.append((start_x, start_y))
        path.append((start_x, start_y))
        cnt += 1
        
        while q:
            x, y = q.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                    continue
                if graph[nx][ny] > height and (nx, ny) not in path:
                    q.append((nx, ny))
                    path.append((nx, ny))
                    cnt += 1
        return True
    return False
                    
