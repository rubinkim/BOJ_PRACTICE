#-*- coding: utf-8 -*-
"""
1
6 5

(yes)
"""
n = int(input())       # 주어지는 자연수 (1 <= n <= 1e5)
k = int(input())       # k-세준수계산을 위한 k

dp = [False] * (n+1)
for num in range(2, n+1):
    prime = True
    for i in range(2, num):
        if num % i == 0:
            prime = False
    if prime:
        dp[num] = True