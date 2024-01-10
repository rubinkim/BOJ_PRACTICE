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
""" 

"""
# dfs 방식
from collections import deque
import sys

def dfs(graph, start):   
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
                
input = sys.stdin.readline    
n, m = map(int, input().split())    
graph = [[] for _ in range(n+1)]
for _ in range(m):
    u, v = map(int, input().split())        
    graph[u].append(v)
    graph[v].append(u) 
    
print(f"graph : {graph}")      

#for row in graph:
    #print(row) 
  
result = []
for i in range(1, n+1):
    x = dfs(graph, i)
    x.sort()
    if x not in result:
        result.append(x)
print(len(result))
"""
"""
from collections import deque
import sys

def dfs(graph, start):   
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
                
input = sys.stdin.readline    
n, m = map(int, input().split())    
graph = {}
for _ in range(m):
    u, v = map(int, input().split())
    if u not in graph:
        graph[u] = [v]
    else:
        graph[u].append(v)
    
    if v not in graph:
        graph[v] = [u]
    else:
        graph[v].append(u) 
            
result = []
cnt = 0

while graph:
    x = dfs(graph, list(graph.keys())[0])
    for j in range(len(x)):
        del graph[x[j]]
    cnt += 1
print(cnt)
"""

from collections import deque
import sys

def dfs(graph, start):
    global path
    q = deque([start])    
    while q:
        now = q.pop()
        if now not in path:
            path.append(now)
        for nxt in reversed(graph[now]):
            if nxt not in path:
                q.append(nxt)
                
input = sys.stdin.readline    
n, m = map(int, input().split())    
graph = [[] for _ in range(n+1)]
path = []

for _ in range(m):
    u, v = map(int, input().split())        
    graph[u].append(v)
    graph[v].append(u) 
    
print(f"graph : {graph}")

result = 0
for i in range(1, n+1):
    if i not in path:
        if not graph:
            result += 1
            path.append(i)
        else:
            dfs(graph, i)
            result += 1
            print(path)
        
print(result)

### 정답
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

N, M = map(int, input().split())
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

# 방문처리
visited = [False] * (1 + N)
count = 0  # 컴포넌트 그래프 개수 저장

# 1~N번 노드를 각각돌면서
for i in range(1, N + 1):
    if not visited[i]:  # 만약 방문하지 않았다면
        bfs(i)  # 해당 i를 시작노드로 bfs를 돈다.
        count += 1  # 연결요소 를 +1개 해준다.

print(count)

                 
    
