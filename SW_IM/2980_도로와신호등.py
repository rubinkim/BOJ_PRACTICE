#-*- coding: utf-8 -*-
"""
2 10
3 5 5
5 2 2

12

4 30
7 13 5
14 4 4
15 3 10
25 1 1

36
"""

N, L = map(int, input().split())
drg = [(0, 0, 0)]
for _ in range(N):
    d, r, g = map(int, input().split())
    drg.append((d, r, g))
    
t = 0

for i in range(1, len(drg)):
    t += drg[i][0] - drg[i-1][0]
    if t - (t // (drg[i][1] + drg[i][2])) * (drg[i][1] + drg[i][2]) < drg[i][1]:
        t = t + (drg[i][1] -t) 
        
    #print(f"i : {i}    t : {t}")

t += L - drg[-1][0]
print(t)   