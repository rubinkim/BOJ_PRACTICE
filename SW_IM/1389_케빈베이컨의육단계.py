"""
5 5
1 3
1 4
4 5
4 3
3 2

(3)
"""

# kevin bacon게임은 임의의 두사람이 최소 몇단계만에 이어질 수 있는지 계산하는 게임이다.
# 케빈베이컨의 수는 모든 사람들과 케빈베이컨게임을 했을 때 나오는 단계의 합이다.
# 유저의 수와 친구 관계가 주어졌을 때 케빈베이컨의 수가 가장 적은 사람을 구하는 프로그램을 작성하라.
# 유저의 번호는 1부터 N까지이며 두사람이 같은 번호를 갖는 경우는 없다. --> 1기반 번호를 0기반 인덱스롤 변경하는 작업이 필요!!!

n, m = map(int, input().split())        # n : 유저의 수,  m : 친구관계의 수
adj = [[] for _ in range(n)]            # adj : 인접리스트
for _ in range(m):
    a, b = map(lambda x : x-1,  map(int, input().split()))
    adj[a].append(b)
    adj[b].append(a)
    
for row in adj:
    print(row)

# 유저들간의 친구관계들은 노드와 간선들로 구성된 그래프이며 우리는 이것을 인접리스트를 이용해서 표현하였다. 
# 노드들간의 최단거리를 구하려면 우리는 bfs를 사용하거나 floyd-warshall 알고리즘을 이용할 수 있다.
# 지금은 bfs를 사용해서 문제를 풀것인데 floyd-warshall로도 꼭 풀어보길 바란다.

from collections import deque

# 1. 어떤 임의의 한 사람으로부터 다른 임의의 한 사람까지의 최단 거리를 구하는 함수
def bfs(start, goal):
    chk = [False] * n        # 어떤 유저를 방문한 적이 있는지 없는지를 체크하는 리스트
    chk[start] = True
    dq = deque()
    dq.append((start, 0))    # 출발하는 유저의 인덱스 & 출발유저와의 거리가 얼마나 되는가를 나타내는 숫자의 튜플로 dq에 저장한다.
    
