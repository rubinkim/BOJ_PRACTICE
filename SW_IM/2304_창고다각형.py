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

mx_i = 0
mx = 0

for i in range(N):
    if lst[i][1] > mx:
        mx = max(mx, lst[i][1])
        mx_i = i
        
print(f"mx_i : {mx_i},  mx : {mx}")

# 오른쪽 면적 계산
area = 0
current_left = lst[0][0]
current_height = lst[0][1]

for i in range(1, mx_i+2):       # mx까지 포함
    if lst[i][1] > current_height:
        previous_left, previous_height = current_left, current_height
        current_left, current_height = lst[i][0], lst[i][1]
        area += (current_left - previous_left) * previous_height
        print(f"i : {i},  previous_left : {previous_left},  current_left : {current_left},  previous_height : {previous_height},  area : {area}")
        
# 왼쪽 면적 계산
current_left = lst[-1][0]
current_height = lst[-1][1]

for i in range(N-1, mx_i-1, -1):
    if lst[i][1] > current_height:
        previous_left, previous_height = current_left, current_height
        current_left, current_height = lst[i][0], lst[i][1]
        area += (previous_left - current_left) * previous_height
        print(f"i : {i},  previous_left : {previous_left},  current_left : {current_left},  previous_height : {previous_height},  area : {area}")
        
print(area)


"""
# 문어박사 풀이방법

N = int(input())
lst = [0] * 1001
mx = 0
mx_i = 0

for _ in range(N):
    L, H = map(int, input().split())
    lst[L] = H
    if mx < H:
        mx_i, mx = L, H


ans = 0
mx = 0
for i in range(mx_i + 1):
    mx = max(mx, lst[i])
    ans += mx
    

mx = 0
for i in range(1000, mx_i, -1):
    mx = max(mx, lst[i])
    ans += mx
    
print(ans)
"""
        
        
    
