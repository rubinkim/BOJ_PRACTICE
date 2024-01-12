#-*- coding: utf-8 -*-
"""
5
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
"""

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    row = input().rstrip()
    for j in range(len(row)):
        graph[i][j] = row[j]
        
for row in graph:
    print(row)

path = []
cc_num_list = []
cnt = 0

def dfs(graph, start_x, start_y, num):
    global path, color_dict, cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    if start_x <= -1 or start_x >= n or start_y <= -1 or start_y >= n:
        return False
    RGB = ["R", "G", "B"]
    if (start_x, start_y) not in path:        
        for color in RGB:
            if graph[start_x][start_y] == color:
                q = deque([(start_x, start_y)])
                path.append((start_x, start_y))
                graph[start_x][start_y] = num
                cnt += 1      
                while q:
                    x, y = q.pop()   
                    for i in range(4):
                        nx = x + dx[i]
                        ny = y + dy[i]
                        if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                            continue
                        if graph[nx][ny] == color and (nx, ny) not in path:
                            q.append((nx, ny))
                            path.append((nx, ny))
                            graph[nx][ny] = num
                            cnt += 1
        return True
    return False
"""
ans = 0
for i in range(n):
    for j in range(n):
        if  dfs(graph, i, j, ans):
            cc_num_list.append(cnt)
            ans +=1
            cnt = 0
print(ans)   
print(cc_num_list)
"""
print(" ".join("abbdc"))
    
    
