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

    dist_lst, weight_lst = [], []
    total_dist, total_weight = 0, 0  
    for i in range(n):
        dist, weight = map(int, input().split())        
        if n == 1:
            total_dist = 2 * dist
            
        elif n > 1:        
            if i == 0 and weight == w:
                total_weight = 0
                total_dist = 3 * dist
                dist_lst.append(dist)
                weight_lst.append(weight) 

            elif i > 0 and weight == w: 
                if total_weight + weight < w:
                    if i == 0:
                        total_weight += weight
                        total_dist += dist
                        dist_lst.append(dist)
                        weight_lst.append(weight)
                    elif 0 < i < n-1:
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
                    if  i == 0:
                        total_weight = 0
                        total_dist += 2 * dist
                        dist_lst.append(dist)
                        weight_lst.append(weight)                                            
                    elif 0 < i < n-1:
                        total_weight = 0
                        total_dist += (dist - dist_lst[-1] + 2 * dist)
                        dist_lst.append(dist)
                        weight_lst.append(weight)
                    elif i == n-1:
                        total_weight = 0
                        total_dist += (dist - dist_lst[-1] + dist)
                        dist_lst.append(dist)
                        weight_lst.append(weight)
                        
                elif total_weight + weight > w:
                    if 0 < i < n-1:
                        total_weight = weight
                        total_dist += (dist - dist_lst[-1] + 2 * dist)
                        dist_lst.append(dist)
                        weight_lst.append(weight)
                    elif i == n-1:
                        total_weight = 0
                        total_dist += (dist - dist_lst[-1] + 3 * dist)
                        dist_lst.append(dist)
                        weight_lst.append(weight)                                 
                  
            elif weight < w: 
                if total_weight + weight < w:
                    if i == 0:
                        total_weight += weight
                        total_dist += dist
                        dist_lst.append(dist)
                        weight_lst.append(weight)
                    elif 0 < i < n-1:
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
                    if  i == 0:
                        total_weight = 0
                        total_dist += 2 * dist
                        dist_lst.append(dist)
                        weight_lst.append(weight)                                            
                    elif 0 < i < n-1:
                        total_weight = 0
                        total_dist += (dist - dist_lst[-1] + 2 * dist)
                        dist_lst.append(dist)
                        weight_lst.append(weight)
                    elif i == n-1:
                        total_weight = 0
                        total_dist += (dist - dist_lst[-1] + dist)
                        dist_lst.append(dist)
                        weight_lst.append(weight)
                        
                elif total_weight + weight > w:
                    if 0 < i < n-1:
                        total_weight = weight
                        total_dist += (dist - dist_lst[-1] + 2 * dist)
                        dist_lst.append(dist)
                        weight_lst.append(weight)
                    elif i == n-1:
                        total_weight = 0
                        total_dist += (dist - dist_lst[-1] + 3 * dist)
                        dist_lst.append(dist)
                        weight_lst.append(weight)
    print(total_dist)
                                   