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
n = int(input())       
k = int(input())       

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
"""
# 내방법은 시간초과!!!
import math
import sys
input = sys.stdin.readline
n = int(input())
k = int(input())
array = [True] * (n+1)
cnt = 0

def is_prime(x):
    for i in range(2, x):
        if x % i == 0:
            return False
    return True

def prime_factors(x):
    lst = []
    for i in range(2, x+1):
        if is_prime(i) and x % i == 0:
            lst.append(i)
    return lst
            
cnt = 1
for i in range(2, n+1):
    if max(prime_factors(i)) <= k:
        cnt += 1

print(cnt)
"""
            
n = int(input())
k = int(input())
                
