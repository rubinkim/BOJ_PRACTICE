#-*- coding: utf-8 -*-
"""
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0

8
0 5 4 5 4 5 4 5
4 0 5 1 2 3 4 5
9 8 0 1 2 3 1 2
9 9 9 0 9 9 9 9
1 1 1 1 0 1 1 1
8 7 6 5 4 0 3 2
9 1 9 1 9 1 0 9
6 5 4 3 2 1 9 0
"""

from itertools import permutations
import sys
input = sys.stdin.readline
N = int(input())
S = [[0] * N for _ in range(N)]
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
        S[i][j] = row[j]
        
for row in S:
    print(row)
    
diff = 1e20
v1, v2 = [0] * N,  [0] * N

def dfs(n, start_score, link_score, start_lst, link_lst):  # n : start_lst에 포함될 사람의 숫자.
    global diff
    if n > int(N / 2):
        for j in range(N):
            if j not in start_lst:
                link_lst.append(j) 
        print(f"n : {n},  start_lst : {start_lst},  link_lst : {link_lst}")
    
        for i, j in permutations(link_lst, 2):
            link_score += S[i][j] 
                
        diff = min(diff, abs(sum(start_lst) - sum(link_lst)))
        return
    
    for i in range(N):
        for j in range(N):
            if S[i][j] not in start_score:
                v1[i] = 1
                v1[j] = 1
                start_lst.append(i)
                start_lst.append(j)
                dfs(n+1, start_score.append(S[i][j]), link_score, start_lst,  link_lst)
                v1[i] = 0
                v1[j] = 0
    
dfs(1, 0, 0, [], [])
print(diff)
    
        
        