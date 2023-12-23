#-*- coding: utf-8 -*-

""" 데이터
4 5 1
1 2
1 3
1 4
2 4
3 4
"""

import sys
input = sys.stdin.readline
n, m, v = map(int, input().split())
print(f"n : {n},  m : {m},  v : {v}")    # n : 노드수,  m : 간선수,  v : 출발노드

graph = [[0] * (m+1) for _ in range(n+1)]
for i in range(1, n+1):
    a, b = map(int, input().split())
    graph[a][b] = graph[b][a] = 1
    
for row in graph:
    print(row)
    
from collections import deque   
# DFS using stack
def dfs_stack(graph, v):
    q = deque([v])
    path = []
    while q:
        now = q.pop()
        if now not in path:
            path.append(now)
        for nxt in graph[now]:
            if nxt not in path:
                q.append(nxt)
    return path

print(f"{v}를 출발노드로 할 때 DFS로 탐색한 경로 : {dfs_stack(graph, v)}")