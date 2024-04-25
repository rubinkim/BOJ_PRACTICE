#-*- coding: utf-8 -*-
"""
15
(4)
"""
left, right = 0, 1
ans, acc = 0, 1

n = int(input())

while left <= right:
    if acc == n:
        ans += 1
        right += 1
        acc += right