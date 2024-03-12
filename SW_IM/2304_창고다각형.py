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

area = 0
current_left = lst[0][0]
current_height = lst[0][1]

mx_i = 0
mx = 0
for i in range(N):
    

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

# ���ʺ��� ó��
ans = 0
mx = 0
for i in range(mx_i + 1):
    mx = max(mx, lst[i])
    ans += mx
    
# ������ ó��
mx = 0
for i in range(1000, mx_i, -1):
    mx = max(mx, lst[i])
    ans += mx
    
print(ans)
"""
        
        
    
