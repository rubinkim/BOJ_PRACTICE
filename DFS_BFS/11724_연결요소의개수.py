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

#for row in graph:
    #print(row)    
result = []
for i in range(1, n+1):
    x = dfs(graph, i)
    x.sort()
    if x not in result:
        result.append(x)
print(len(result))
