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
    graph.append(input().rstrip())

path = []
color_dict = {}

def dfs(graph, start_x, start_y):
    global path, color_dict, cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    if start_x <= -1 or start_x >= n or start_y <= -1 or start_y >= n:
        return False
    RGB = ["R", "G", "B"]
    for color in RGB:
        if graph[start_x][start_y] == color and (start_x, start_y) not in path:
            q = deque([(start_x, start_y)])
            path.append((start_x, start_y))
            if color not in color_dict.keys():
                color_dict[color] = 1
            else:
                color_dict[color] += 1        
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
                    color_dict[color] += 1
        return True
    return False

ans = 0


for c in rgb:
    for i in range(n):
        for j in range(n):
            if     
        
    
    
