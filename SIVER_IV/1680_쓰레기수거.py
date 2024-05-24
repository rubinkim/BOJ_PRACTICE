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
dist_lst, weight_lst = [], []
total_dist, total_weight = 0, 0

w, n = map(int, input().split())
dist, weight = map(int, input().split())
dist_lst.append(dist)
weight_lst.append(weight)
total_dist += dist
total_weight += weight

if n == 1:
    print(total_dist)
else:
        
