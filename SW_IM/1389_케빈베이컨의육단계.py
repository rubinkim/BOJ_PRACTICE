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
