#-*- coding: utf-8 -*-
"""
4 4
0100
0111
1110
0010

(4)
"""

n, m = map(int, input().split())
arr = [[0] * m for _ in range(n)]
dp = [[0] * m for _ in range(n)]