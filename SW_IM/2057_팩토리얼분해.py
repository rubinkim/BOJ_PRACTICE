#-*- coding: utf-8 -*-
"""
5

NO
"""

left, right = 0, 0
ans, acc = 0, 0

n = int(input())

while left <= right:
    if acc == n:
        print("YES")
        break
    elif acc > n:
        right += 1
        acc += dp[right]
    elif acc < n:
        acc -= dp[left]
        left += 1
        
if left > right:
    print("NO")