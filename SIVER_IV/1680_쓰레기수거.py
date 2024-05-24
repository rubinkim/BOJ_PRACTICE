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
    for i in range(n-1):
        dist, weight = map(int, input().split())
        if total_weight + weight < w:
            total_weight += weight
            total_dist += (dist - dist_lst[-1])
            weight_lst.append(weight)
            dist_lst.append(dist)
        elif total_weight + weight == w:
            if len(dist_lst) < n-1:          
                total_weight = 0
                total_dist += dist - dist_lst[-1] + 2 * dist
                weight_lst.append(weight)
                dist_lst.append(dist)     
            elif len(dist_lst) == n-1:
                total_weight = 0
                total_dist += dist - dist_lst[-1] + dist
                weight_lst.append(weight)
                dist_lst.append(dist)       
        elif total_weight + weight > w:
            if len(dist_lst) < n-1:                
                total_weight = weight
                total_dist += dist - dist_lst[-1] + 2 * dist
                weight_lst.append(weight)
                dist_lst.append(dist)
            elif len(dist_lst) == n-1:
                total_weight = 0
                total_dist += dist - dist_lst[-1] + dist
                weight_lst.append(weight)
                dist_lst.append(dist)

            
print(total_dist)
            
