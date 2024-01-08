#-*- coding: utf-8 -*-

"""
  시간 제한	   메모리 제한	  제출	   정답	    맞힌 사람	    정답 비율
    3 초	     512 MB	    119359	 53835	    35406	      42.146%   
  
방향 없는 그래프가 주어졌을 때, 연결 요소 (Connected Component)의 개수를 구하는 프로그램을 작성하시오.

입력 : 첫째 줄에 정점의 개수 N과 간선의 개수 M이 주어진다. (1 ≤ N ≤ 1,000, 0 ≤ M ≤ N*(N-1)/2) 둘째 줄부터 M개의 줄에 간선의 양 끝점 u와 v가 주어진다. 
      (1 ≤ u, v ≤ N, u ≠ v) 같은 간선은 한 번만 주어진다.
출력 : 첫째 줄에 연결 요소의 개수를 출력한다.  답 : (2,  1)

6 5
1 2
2 5
5 1
3 4
4 6

6 8
1 2
2 5
5 1
3 4
4 6
5 4
2 4
2 3
""" 

# dfs 방식
from collections import deque
import sys

def connected_component_mutant(graph, start_y, start_x, num):
    global path, num_dict
    dy, dx = [0, 0, -1, 1], [-1, 1, 0, 0]    
    q = deque()    
    if start_x <= -1 or start_x >= m or start_y <= -1 or start_y >= n:
        return False
    if graph[start_y][start_x] == 0:
        return False
    if graph[start_y][start_x] == 1 and (start_y, start_x) in path:
        return False    
    if graph[start_y][start_x] == 1 and (start_y, start_x) not in path:
        q.append((start_y, start_x))
        path.append((start_y, start_x))
        graph[start_y][start_x] = num
        if num not in num_dict:
            num_dict[num] = 1
        else:
            num_dict[num] += 1
        
        while q:
            y, x = q.pop()                     # x, y = q.popleft()로 하면 bfs이다.
            cnt = 0
            
            for i in range(4):                
                ny = y + dy[i]
                nx = x + dx[i]                
                if ny <= -1 or ny >= n or nx <= -1 or nx >= m:
                    continue
                if graph[ny][nx] == 0:
                    continue
                if graph[ny][nx] == 1 and (ny, nx) in path:
                    continue
                if graph[ny][nx] == 1 and (ny, nx) not in path:
                    q.append((ny, nx))
                    path.append((ny, nx))
                    graph[ny][nx] = num
                    cnt += 1
                    num_dict[num] += 1        
        return True
    return False

input = sys.stdin.readline
    
n, m = map(int, input().split())    
graph = [[0] * (n+1) for _ in range(n+1)]
path = []
num_dict = {}
for _ in range(m):
    u, v = map(int, input().split())        
    graph[u][v] = 1  
    graph[v][u] = 1
      
ans = 1
for i in range(1, n+1):
    for j in range(1, n+1):
        if connected_component_mutant(graph, i, j, ans) == True:
            ans += 1  
print(ans - 1)
