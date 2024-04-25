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

left, right = 0, 0
ans, acc = 0, 0

n = int(input())

while left <= right:
    if acc == n:
        print("YES")
        break
    elif acc > n:
        right += 1
        acc += factorial(right)
    elif acc < n:
        acc -= factorial(left)
        left += 1
        
if left > right:
    print("NO")