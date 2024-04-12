#-*- coding: utf-8 -*-
"""
10
3
(7)
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
for num in range(2, n+1):
    for i in range(2, num):
        if dp[i] and i <= k and num % i == 0:
            cnt += 1
            print(f"{num} : {i}")
print(cnt)