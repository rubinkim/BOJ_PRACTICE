#-*- coding: utf-8 -*-
"""
5

NO
"""

def factorial(x):
    global dp
    if x == 0 or x == 1:
        return 1
    dp[x] = x * factorial(x-1)
    return dp[x]

dp = [1] * (21)

n = int(input())

fac_20 = factorial(20)
sum = 0

for i in range(20, -1, -1):
    if sum + dp[i] < n:
        sum += dp[i]
    