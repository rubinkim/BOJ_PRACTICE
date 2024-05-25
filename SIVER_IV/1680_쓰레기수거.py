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
    for i in range(n):
        dist_lst, weight_lst = [], []
        total_dist, total_weight = 0, 0
        dist, weight = map(int, input().split())
        
        if weight == w:
            total_weight = 0            
            if n == 1:
                total_dist = 2 * dist
            elif n > 1:
                total_dist = 3 * dist
            dist_lst.append(dist)
            weight_lst.append(weight)
                
        elif weight < w: 
            if total_weight + weight < w:
                if i < n-1:
                    total_weight += weight
                    total_dist += (dist - dist_lst[-1])
                    dist_lst.append(dist)
                    weight_lst.append(weight)
                elif i == n-1:
                    total_weight = 0
                    total_dist += (dist - dist_lst[-1] + dist)
                    dist_lst.append(dist)
                    weight_lst.append(weight)
            elif total_weight + weight == w:
                if i < n-1:
                    total_weight = 0
                    
                                   