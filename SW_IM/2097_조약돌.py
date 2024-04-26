#-*- coding: utf-8 -*-
"""
5
(6)

14
(12)
"""
import math
max_i = round((math.log(5) + 8 * math.log(10)) / math.log(2)) + 1
#print(max_i)

n = int(input())
for i in range(1, max_i):
    if i == 1:
        if 1 <= n <= (i+1) ** 2:
            print(4 * i)
    elif i > 1:
        if i ** 2 + 1 <= n <= (i+1) ** 2:
            print(4 * i)
        
