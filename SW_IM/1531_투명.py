#-*- coding: utf-8 -*-
"""
3 1
21 21 80 80
41 41 60 60
71 71 90 90

(500)
"""

n, m = map(int, input().split())
board = [[1] * 100 for _ in range(100)]
for _ in range(n):
    xd, yd, xu, yu = map(int, input().split())
    for i in range(yd, yu+1):
        for j in range(xd, xu+1):
            board[i][j] += 1
            
ans = 0
for i in range(100):
    for j in range(100):
        