#-*- coding: utf-8 -*-

"""
 시간 제한	  메모리 제한	제출	정답	 맞힌 사람	   정답 비율
    1 ��	    128 MB	  160129	74227	49918	     45.851%
  
신종 바이러스인 웜 바이러스는 네트워크를 통해 전파된다. 한 컴퓨터가 웜 바이러스에 걸리면 그 컴퓨터와 네트워크 상에서 연결되어 있는 모든 컴퓨터는 웜 바이러스에 걸리게 된다.
예를 들어 7대의 컴퓨터가 <그림 1>과 같이 네트워크 상에서 연결되어 있다고 하자. 1번 컴퓨터가 웜 바이러스에 걸리면 웜 바이러스는 2번과 5번 컴퓨터를 거쳐 3번과 6번 컴퓨터까지 
전파되어 2, 3, 5, 6 네 대의 컴퓨터는 웜 바이러스에 걸리게 된다. 하지만 4번과 7번 컴퓨터는 1번 컴퓨터와 네트워크상에서 연결되어 있지 않기 때문에 영향을 받지 않는다.
어느 날 1번 컴퓨터가 웜 바이러스에 걸렸다. 컴퓨터의 수와 네트워크 상에서 서로 연결되어 있는 정보가 주어질 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 출력하는 
프로그램을 작성하시오.

입력 : 첫째 줄에는 컴퓨터의 수가 주어진다. 컴퓨터의 수는 100 이하인 양의 정수이고 각 컴퓨터에는 1번 부터 차례대로 번호가 매겨진다.
      둘째 줄에는 네트워크 상에서 직접 연결되어 있는 컴퓨터 쌍의 수가 주어진다. 이어서 그 수만큼 한 줄에 한 쌍씩 네트워크 상에서 직접 연결되어 있는 컴퓨터의 번호 쌍이 주어진다.
출력 : 1번 컴퓨터가 웜 바이러스에 걸렸을 때, 1번 컴퓨터를 통해 웜 바이러스에 걸리게 되는 컴퓨터의 수를 첫째 줄에 출력한다.

7
6
1 2
2 3
1 5
5 2
5 6
4 7         4
"""

from collections import deque
import sys
input = sys.stdin.readline

v = int(input())
e = int(input())

graph = {}
for _ in range(e):
      a, b = map(int, input().split().rstrip())
      if a not in graph.keys():
            graph[a] = [b]
      else:
            graph[a].append(b)
      if b not in graph.keys():
            graph[b] = [a]
      else:
            graph[b].append(a)
            
def dfs_deque(graph, start):
    q = deque([start])
    path = []
    while q:
        now = q.pop()
        if now not in path and now != start:
            path.append(now)
        for nxt in graph[now]:
            if nxt not in path:
                q.append(nxt)
    print(len(path))

dfs_deque(graph, 1)