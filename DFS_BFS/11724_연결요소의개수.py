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

# 諛⑸Ц泥섎━
visited = [False] * (1 + n)
cnt = 0  # 而댄룷�꼳�듃 洹몃옒�봽 媛쒖닔 ����옣

# 1~N踰� �끂�뱶瑜� 媛곴컖�룎硫댁꽌
for i in range(1, n + 1):
    if not visited[i]:  # 留뚯빟 諛⑸Ц�븯吏� �븡�븯�떎硫�
        if not graph[i]:           # 留뚯빟 洹몃옒�봽媛� 鍮꾩뼱�엳�떎硫�
            cnt += 1             # 媛쒖닔 �븳媛� 異붽��
            visited[i] = True      # 諛⑸Ц泥섎━
        else:
            bfs(graph, i)  # �빐�떦 i瑜� �떆�옉�끂�뱶濡� bfs瑜� �룉�떎.
            cnt += 1  # �뿰寃곗슂�냼 瑜� +1媛� �빐以��떎.

print(cnt)
"""
"""    
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
    
for row in graph:
    print(row)
print()

# 諛⑸Ц泥섎━
path = []
cnt = 0  # 而댄룷�꼳�듃 洹몃옒�봽 媛쒖닔 ����옣

# 1~N踰� �끂�뱶瑜� 媛곴컖�룎硫댁꽌
for i in range(1, n + 1):
    if i not in path:  # 留뚯빟 諛⑸Ц�븯吏� �븡�븯�떎硫�
        if not graph[i]:           # 留뚯빟 洹몃옒�봽媛� 鍮꾩뼱�엳�떎硫�
            cnt += 1               # 媛쒖닔 �븳媛� 異붽��
            path.append(i)         # 諛⑸Ц泥섎━
            print(path)
        else:
            dfs(graph, i)  # �빐�떦 i瑜� �떆�옉�끂�뱶濡� bfs瑜� �룉�떎.
            cnt += 1  # �뿰寃곗슂�냼 瑜� +1媛� �빐以��떎.
            print(path)

print(cnt)               
"""

"""
### BFS using path
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

# 諛⑸Ц泥섎━
path = []
cnt = 0  # 而댄룷�꼳�듃 洹몃옒�봽 媛쒖닔 ����옣

# 1~N踰� �끂�뱶瑜� 媛곴컖�룎硫댁꽌
for i in range(1, n + 1):
    if i not in path:  # 留뚯빟 諛⑸Ц�븯吏� �븡�븯�떎硫�
        if not graph[i]:           # 留뚯빟 洹몃옒�봽媛� 鍮꾩뼱�엳�떎硫�
            cnt += 1               # 媛쒖닔 �븳媛� 異붽��
            path.append(i)         # 諛⑸Ц泥섎━
        else:
            bfs(graph, i)  # �빐�떦 i瑜� �떆�옉�끂�뱶濡� bfs瑜� �룉�떎.
            cnt += 1  # �뿰寃곗슂�냼 瑜� +1媛� �빐以��떎.
            print(path)

print()
print(cnt) 
"""     

import sys
from collections import deque
sys.setrecursionlimit(5000)

input = sys.stdin.readline


