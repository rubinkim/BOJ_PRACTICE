#-*- coding: utf-8 -*-
"""
3
2 2
1 1
2 2
6 3
1 1
2 2
3 3
3 3
1 2
2 2
3 1

(8
6
10)
"""

t = int(input())

for _ in range(t):
    w, n = map(int, input().split())
    for _ in range(n):
        dist_lst, weight_lst = [], []
        total_dist, total_weight = 0, 0
        dist, weight = map(int, input().split())
        
        if weight == w:
            