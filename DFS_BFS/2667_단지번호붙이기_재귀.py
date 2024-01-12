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
cnt = 0

def dfs_recursion(graph, start_x, start_y, num):
    global cnt
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]    
    
    if start_x <= -1 or start_x >= n or start_y <= -1 or start_y >= n:
        return False
    if graph[start_x][start_y] == 0:
        #print(f"start_x : {start_x}, start_y : {start_y}")
        return False
    if graph[start_x][start_y] == 1 and (start_x, start_y) in path:
        return False
    if graph[start_x][start_y] == 1 and (start_x, start_y) not in path:
        path.append((start_x, start_y))
        graph[start_x][start_y] = num
        cnt += 1

        for i in range(4):
            nx, ny = start_x + dx[i], start_y + dy[i]
            if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1 and (nx, ny) in path:
                continue
            if graph[nx][ny] == 1 and (nx, ny) not in path:
                dfs_recursion(graph, nx, ny, num)
        return True
    return False

ans = 0
for i in range(n):
    for j in range(n):
        print(f"i : {i},  j : {j}")
        if dfs_recursion(graph, i, j, ans+1):
            path.append(cnt)
            ans += 1
            cnt = 0

path.sort()
print(ans)
for i in range(len(path)):
    print(path[i])