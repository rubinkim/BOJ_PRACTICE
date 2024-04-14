#-*- coding: utf-8 -*-
"""
2143
(4321)

999998999
(999999998)

61423
(64321)

500613009
(965310000)
"""

n = list(input())
for i in range(len(n)):
    for j in range(i+1, n):
        if n[i] < n[j]:
            n[i], n[j] = n[j], n[i]

print(n)