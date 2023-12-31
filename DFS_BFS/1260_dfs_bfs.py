#-*- coding: utf-8 -*-

""" 데이터
4 5 1
1 2
1 3
1 4
2 4
3 4

5 5 3
5 4
5 2
1 2
3 4
3 1


1000 1 1000
999 1000

"""

"""
# 1. Get the data
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
    row.sort()

for row in graph:
    print(row)
    
from collections import deque   

# 2. DFS using stack
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
    
# 3. DFS using recursion
path = []
def dfs_recursion(graph, start):
    global path
    path.append(start)
    
    for nxt in graph[start]:
        if nxt not in path:
            dfs_recursion(graph, nxt)

# 4. BFS using queue
def bfs_queue(graph, start):
    q = deque([start])
    path = []
    while q:
        now = q.popleft()
        if now not in path:
            path.append(now)
        for nxt in graph[now]:
            if nxt not in path:
                q.append(nxt)
    return path 
    
# 4. 해답 구하기
print()
print(f"{v}를 출발노드로 할 때 DFS로 탐색한 경로 : {dfs_stack(graph, v)}")

print()
dfs_recursion(graph, v)
for x in path:
    print(x, end=' ')

print()
print(f"{v}를 출발노드로 할 때 BFSFH 탐색할 경로 : {bfs_queue(graph, v)}")
"""


# 1. Get the data
import sys
input = sys.stdin.readline
n, m, v = map(int, input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for row in graph:
    row.sort()
    
from collections import deque   

# 2. DFS using stack
def dfs_stack(graph, start):
    q = deque([start])
    path = []    
    while q:
        now = q.pop()
        if now not in path:
            path.append(now)
            print(now, end=' ')
        for nxt in reversed(graph[now]):
            if nxt not in path:
                q.append(nxt)
                
# 3. DFS using recursion
path = []
def dfs_recursion(graph, start):
    global path
    path.append(start)
    
    for nxt in graph[start]:
        if nxt not in path:
            dfs_recursion(graph, nxt)
    

# 4. BFS using queue
def bfs_queue(graph, start):
    q = deque([start])
    path = []
    while q:
        now = q.popleft()
        if now not in path:
            path.append(now)
            print(now, end=' ')
        for nxt in graph[now]:
            if nxt not in path:
                q.append(nxt)
    
# 4. 해답 구하기
#dfs_stack(graph, v)
#print()
dfs_recursion(graph, v)
for x in path:
    print(x, end=' ')
print()
bfs_queue(graph, v)
