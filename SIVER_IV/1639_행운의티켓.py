#-*- coding: utf-8 -*-
"""
74233285
(4)

123231
(6)

986561517416921217551395112859219257312
(36)

1
(0)

112
(2)
"""
s = list(input())
half = len(s) // 2
if len(s) % 2 == 0:
    

while True:
    decrement = 0
    half = (len(s) - decrement) // 2
    ans = 0
    
    if len(s) % 2 == 0:
        if sum(s[0:half]) == sum(s[half, 2*half]):
            ans = 2 * half
        else:
            decrement += 2
            