#-*- coding: utf-8 -*-
"""
7
2 4
11 4
15 8
4 6
5 3
8 10
13 6

98
"""

N = int(input())
lst = []
for _ in range(N):
    left, height = map(int, input().split())
    lst.append((left, height))
    
lst.sort(key=lambda x : x[0])
print(lst)

L, H = [], []
for l, h in lst:
    L.append(l)
    H.append(h)
    
print(L)
print(H)

current_height = H[0]
current_left = L[0]
area = 0

for i in range(len(L)):
    current_idx = i
    if H[current_idx] == max(H[current_idx:]):
        next_idx = H.index(max(H[current_idx+1:]))
        area += H[current_idx] + (next_idx - current_idx - 1) * H[next_idx]
    elif H[current_idx] < max(H[current_idx:]) and H[current_idx] <= H[current_idx + 1]:
        area += H[current_idx] * 1
    elif H[current_idx] < max(H[current_idx:]) and H[current_idx] > H[current_idx + 1]:
        continue
        
print(area)


        
    
