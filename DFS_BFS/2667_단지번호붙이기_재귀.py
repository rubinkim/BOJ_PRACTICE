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

n = int(input())       # 정사각형의 가로 세로 크기
graph = []             # 가로세로크기가 n인 정사각형의 지도
path = []              # 방문처리를 위한 리스트
cc_num_list = []       # 각각의 연결요소마다의 크기를 저장하는 리스트
cnt = 0                # 각각의 연결요소에 1이 몇개가 있는지를 나타내는 변수
for _ in range(n):
    graph.append(list(map(int, input().rstrip())))

def dfs_recursion(graph, start_x, start_y, num):
    global cnt
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
        cnt += 1

        for i in range(4):
            nx = start_x + dx[i]
            ny = start_y + dy[i]
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
        if dfs_recursion(graph, i, j, ans+1):
            cc_num_list.append(cnt)
            ans += 1
            cnt = 0

print()           
for row in graph:
    print(row)
print()

cc_num_list.sort()
print(ans)
for i in range(len(cc_num_list)):
    print(cc_num_list[i])