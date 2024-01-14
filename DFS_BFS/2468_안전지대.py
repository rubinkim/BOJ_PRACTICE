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
# use visited instead of path (2 -> 19)
# if possible, initialize height_set = {0} instead of using conditional statement inside for loop such as if i == 0: height_set = {graph[i]}, 
# else: height_set = height_set | set(graph[i]) (from 69 -> 100)
# Just use ans_list.append(ans) instead of if ans < max(ans_list): break, else: ans_list.append(ans)

from collections import deque
import sys
input = sys.stdin.readline

n = int(input())
graph = []
height_set = {0}
for i in range(n):
    graph.append(list(map(int, input().split())))
    height_set = height_set | set(graph[i])

#print(f"height_set : {height_set}")

visited = [[False] * n for _ in range(n)]
cc_num_list = []
cnt = 0
    
def dfs(graph, start_x, start_y, height):
    global cnt
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    q = deque()
    
    if start_x <= -1 or start_x >= n or start_y <= -1 or start_y >= n:
        return False
    if graph[start_x][start_y] > height and not visited[start_x][start_y]:
        q.append((start_x, start_y))
        visited[start_x][start_y] = True
        cnt += 1
        
        while q:
            x, y = q.pop()
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if nx <= -1 or nx >= n or ny <= -1 or ny >= n:
                    continue
                if graph[nx][ny] > height and not visited[nx][ny]:
                    q.append((nx, ny))
                    visited[nx][ny] = True
                    cnt += 1
        return True
    return False

ans_list = [0]
for h in list(height_set)[::-1]:
    ans = 0
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if dfs(graph, i, j, h):
                ans += 1
                cnt = 0
    ans_list.append(ans)
    
#print(ans_list)
print(max(ans_list))