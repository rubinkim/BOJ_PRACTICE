#-*- coding: utf-8 -*-
"""
7
3 10
5 20
1 10
1 20
2 15
4 40
2 200

10
1 1
1 2
1 3
1 4
1 5
1 6
1 7
1 8
1 9
1 10
"""

import sys
input = sys.stdin.readline
N = int(input())
T = [0] * N
P = [0] * N

for _ in range(N):
    t, 