#-*- coding: utf-8 -*-

"""
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


### BFS using visited
import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start):
    q = deque([start])
    while q:
        now = q.popleft()
        if not visited[now]:
            visited[now] = True
        for nxt in graph[now]:
            if not visited[nxt]:
                visited[nxt] = True
                q.append(nxt)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문처리
visited = [False] * (1 + n)
cnt = 0  # 컴포넌트 그래프 개수 저장

# 1~N번 노드를 각각돌면서
for i in range(1, n + 1):
    if not visited[i]:  # 만약 방문하지 않았다면
        if not graph[i]:           # 만약 그래프가 비어있다면
            cnt += 1             # 개수 한개 추가
            visited[i] = True      # 방문처리
        else:
            bfs(graph, i)  # 해당 i를 시작노드로 bfs를 돈다.
            cnt += 1  # 연결요소 를 +1개 해준다.

print(cnt)

### DFS using path
import sys
from collections import deque
input = sys.stdin.readline

def dfs(graph, start):
    q = deque([start])
    while q:
        now = q.pop()
        if now not in path:
            path.append(now)
        for nxt in reversed(graph[now]):
            if nxt not in path:
                path.append(nxt)
                q.append(nxt)

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문처리
path = []
cnt = 0  # 컴포넌트 그래프 개수 저장

# 1~N번 노드를 각각돌면서
for i in range(1, n + 1):
    if i not in path:  # 만약 방문하지 않았다면
        if not graph[i]:           # 만약 그래프가 비어있다면
            cnt += 1               # 개수 한개 추가
            path.append(i)         # 방문처리
        else:
            dfs(graph, i)  # 해당 i를 시작노드로 bfs를 돈다.
            cnt += 1  # 연결요소 를 +1개 해준다.

print(cnt)               
"""

import sys
from collections import deque
input = sys.stdin.readline

def bfs(graph, start):
    q = deque([start])
    while q:
        now = q.popleft()
        if now not in path:
            path.append(now)
        for nxt in graph[now]:
            if nxt not in path:
                path.append(nxt)
                q.append(nxt)        

n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)
    
for row in graph:
    print(row)
print()

# 방문처리
path = []
cnt = 0  # 컴포넌트 그래프 개수 저장

# 1~N번 노드를 각각돌면서
for i in range(1, n + 1):
    if i not in path:  # 만약 방문하지 않았다면
        if not graph[i]:           # 만약 그래프가 비어있다면
            cnt += 1               # 개수 한개 추가
            path.append(i)         # 방문처리
        else:
            bfs(graph, i)  # 해당 i를 시작노드로 bfs를 돈다.
            cnt += 1  # 연결요소 를 +1개 해준다.
            print(path)

print()
print(cnt)      
