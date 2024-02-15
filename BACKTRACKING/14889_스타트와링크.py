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
    
sm_dict = {}
for i in range(1, N+1):
    for j in range(i+1, N+1):
        sm_dict[(i,j)] = S[i-1][j-1] + S[j-1][i-1]
print(sm_dict)    

from collections import OrderedDict
x = OrderedDict(ms_dict)
print(x)