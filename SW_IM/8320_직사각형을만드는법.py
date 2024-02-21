#-*- coding: utf-8 -*-

"""
6

8
"""

N = int(input())
cnt = 0
for n in range(1, N+1):
    for i in range(n, int(N/n) + 1):
        if n * i <= N:
            cnt += 1
            
print(cnt)