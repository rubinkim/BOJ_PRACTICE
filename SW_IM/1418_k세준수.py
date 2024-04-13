#-*- coding: utf-8 -*-
"""
10
3
(7)

10
4
(7)

15
3
(8)

5
20
(5)

100000
100
(17442)
"""
"""
n = int(input())       # 주어지는 자연수 (1 <= n <= 1e5)
k = int(input())       # k-세준수계산을 위한 k

dp = [False] * (n+1)
primes = []
for num in range(2, n+1):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    if prime:
        dp[num] = True
        primes.append(num)
print(primes)

cnt = 0
final_lst = []
for num in range(2, n+1):
    max_lst = []
    for i in range(2, num+1):        
        if dp[i] and i <= k and num % i == 0:
            #cnt += 1
            #print(f"{num} : {i}")
            max_lst.append(i)
    print(f"{num}, {max_lst}")
    if max_lst != []:
        final_lst.append(max(max_lst))          
            
            
print(len(final_lst))
"""

import math
import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
array = [True] * (n+1)

cnt = 0
for i in range(2, int(math.sqrt(n))+1):
    j = 2
    max_prime = 0
    while i*j <= n:
        if i*j > n:
            break
        if array[i*j]:
            array[i*j] = False
            if max_prime <= k:
                max_prime = max(max_prime, j)
    if max_prime:
        cnt += 1  
print(cnt)    