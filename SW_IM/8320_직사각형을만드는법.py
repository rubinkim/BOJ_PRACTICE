#-*- coding: utf-8 -*-

"""
6

8

# 1. 가능한 모든 경우를 순회 : 이중 for문을 이용한다.
N = int(input())
cnt = 0
for n in range(1, N+1):
    for i in range(n, int(N/n) + 1):
        if n * i <= N:
            cnt += 1
            
print(cnt)
"""
# 2. 몫연산을 통해서 처리한다. --> 단순 for 문을 이용한다.
N = int(input())
cnt = N

for i in range(2, N):
    n = N // i - (i - 1)
    
print(cnt)

