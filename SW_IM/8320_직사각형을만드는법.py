#-*- coding: utf-8 -*-

"""
6

8
"""

N = int(input())
cnt = 0
for n in range(1, N+1):
    for i in range(1, n//2+1):
        if n % i == 0:
            cnt += 1
            
print(cnt)