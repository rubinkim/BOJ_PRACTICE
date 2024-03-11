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
    
print(f"L : {L}")
print(f"H : {H}")

area = 0
current_idx = 0

while current_idx <= len(H)-1:
    print(f"{H[current_idx]}, {[H[x] for x in range(current_idx+1, N)]}")
    if any([H[x] > H[current_idx] for x in range(current_idx+1, N)]):
        first_idx = [x for x in range(current_idx+1, N) if H[x] > H[current_idx]][0]
        print(f"first_idx : {first_idx}")

        area += (L[first_idx] - L[current_idx]) * H[current_idx]
        print(f"current_idx : {current_idx}, area : {area}")
        current_idx = first_idx
        
    elif all([H[current_idx] > H[x] for x in range(current_idx+1, N)]):
        first_idx = H.index(max(H[current_idx+1 : N]))
        area = area + H[current_idx] * 1 + (L[first_idx] - L[current_idx] - 1) * H[first_idx]
        print(f"current_idx : {current_idx}, area : {area}")
        current_idx = first_idx
        
print(area)
        
        
    
