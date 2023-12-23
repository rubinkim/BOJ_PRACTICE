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

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for row in graph:
    print(row)
    
from collections import deque   
# DFS using stack
def dfs_stack(graph, start):
    q = deque([start])
    path = []
    while q:
        now = q.pop()
        if now not in path:
            path.append(now)
        for nxt in reversed(graph[now]):
            if nxt not in path:
                q.append(nxt)
    return path

#print(f"{v}를 출발노드로 할 때 DFS로 탐색한 경로 : {dfs_stack(graph, v)}")
print(dfs_stack(graph, 1))