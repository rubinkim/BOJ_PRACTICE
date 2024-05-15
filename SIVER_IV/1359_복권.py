#-*- coding: utf-8 -*-
"""
3 1 1
(0.3333333333333333)

3 2 1
(1.0)

8 2 1
(0.4642857142857143)

8 4 2
(0.7571428571428571)
"""

# 1359_lottery

from itertools import combinations
n, m, k = map(int, input().split())
combis = []

for combi in combinations(range(1, n+1), m):
    combis.append(combi)

#print(len(combis))

#for comb in combis:
    #print(comb)
    
cnt = 0
for x in combis:
    for y in combis:
        if len(set(x).intersection(set(y))) >= k:
             cnt += 1
#print(cnt)

print(cnt / len(combis) ** 2)