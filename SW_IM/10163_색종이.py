#-*- coding: utf-8 -*-

"""
2
0 0 10 10
2 2 6 6

64 36


3
0 2 10 10
7 9 8 4
8 4 10 6

81 25 60


4
0 2 10 10
7 9 8 4
8 4 10 6
6 0 12 10

62 24 0 120
"""

N = int(input())
arr = [[0] * 1002 for _ in range(1002)]

for num in range(1, N+1):
    sj, si, w, h = map(int, input().split())
    for i in range(si, si+h):
        for j in range(sj, sj+w):
            arr[i][j] = num
    