#-*- coding: utf-8 -*-

"""
7 6
11

7 6
87

100 100
3000


6 6
0
9 64
"""

C, R = map(int, input().split())
K = int(input())

board = [[0] * C for _ in range(R)]
