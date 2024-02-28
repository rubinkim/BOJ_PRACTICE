#-*- coding: utf-8 -*-

"""
10
3
2 4
7 8
6 9

10
3
1 3
5 7
8 9

10
5
1 1
1 2
1 3
1 4
7 8


3   1   4
1   1   5
"""
L = int(input())
N = int(input())

cakes = [0] * (L+1)
audience_dict = {}

for i in range(N):
    p, k = tuple(map(int, input().split()))
    audience_dict[i+1] = k - p + 1
    for j in range(p, k+1):
        if cakes[j] == 0:
            cakes[j] = i+1
            
print(audience_dict)
print(cakes)
    
