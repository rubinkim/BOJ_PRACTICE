#-*- coding: utf-8 -*-

"""
7
0110100
0110101
1110101
0000111
0100000
0111110
0111000
                   
"""

import sys
input = sys.stdin.readline

n = int(input())
graph = []
path = []
num_dict, cell_dict = {}, {}

def dfs_recursion(graph, start_x, start_y, num, depth):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    
    if start_x <= -1 or start_x >= n or start_y <= -1 or start_y >= n:
        return False
    if graph[start_x][start_y] == 0:
        return False
    if graph[start_x][start_y] == 1 and (start_x, start_y) in path:
        return False
    if graph[start_x][start_y] == 1 and (start_x, start_y) not in path:
        path.append((start_x, start_y))
        graph[start_x][start_y] = num
        if num not in num_dict.keys():
            num_dict[num] = 1
        if num not in cell_dict.keys():
            cell_dict[num] = [(start_x, start_y)]
        
        cnt = 0
        for i in range(4):
            nx, ny = start_x + dx[i], start_y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1 and (nx, ny) in path:
                continue
            if graph[nx][ny] == 1 and (nx, ny) not in path:
                dfs_recursion(graph, nx, ny, num, depth+1)
                cnt += 1
                num_dict[num] += 1
                cell_dict[num].append((nx, ny))
        return True
    return False

ans = 0
for i in range(n):
    for j in range(n):
        if graph[i][j] == 1 and (i, j) not in path:
            ans += 1
            dfs_recursion(graph, i, j, ans+1, 0)
print(ans)