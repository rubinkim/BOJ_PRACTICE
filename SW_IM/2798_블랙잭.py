#-*- coding: utf-8 -*-

"""
5 21
5 6 7 8 9

10 500
93 181 245 214 315 36 185 138 216 295

21 497
"""

from itertools import combinations
N, M = map(int, input().split())
lst = list(map(int, input().split()))
ans = 0

for x in combinations(lst, 3):
    #print(f"x : {x},  sum of x : {sum(x)}")
    if sum(x) <= M:
        ans = max(ans, sum(x))
        
print(ans)
