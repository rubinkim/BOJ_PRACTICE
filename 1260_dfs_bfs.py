#-*- coding: utf-8 -*-

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