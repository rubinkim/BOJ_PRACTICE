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


N = int(input())
lst = []
for _ in range(N):
    left, height = map(int, input().split())
    lst.append((left, height))
    
lst.sort(key=lambda x : x[0])

L, H = [], []
for l, h in lst:
    L.append(l)
    H.append(h)
    
area = 0
current_idx = 0

while current_idx <= len(H)-1:
    if current_idx == len(H)-1:
        break

    if any([H[x] > H[current_idx] for x in range(current_idx+1, N)]):
        first_idx = [x for x in range(current_idx+1, N) if H[x] > H[current_idx]][0]

        area += (L[first_idx] - L[current_idx]) * H[current_idx]
        current_idx = first_idx
        
    elif all([H[current_idx] > H[x] for x in range(current_idx+1, N)]):
        first_idx = H.index(max(H[current_idx+1 : N]))
        area = area + H[current_idx] * 1 + (L[first_idx] - L[current_idx]) * H[first_idx]
        current_idx = first_idx
        
print(area)
"""

N = int(input())
lst = [0] * 1001
mx = 0
mx_i = 0

for _ in range(N):
    L, H = map(int, input().split())
    lst[L] = H
    if mx < H:
        mx_i, mx = L, H

# 哭率何磐 贸府
ans = 0
mx = 0
for i in range(mx_i + 1):
    mx = max(mx, lst[i])
    ans += mx
    


        
        
    
