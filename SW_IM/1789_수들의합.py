#-*- coding: utf-8 -*-
"""
200

19
"""
x = list(range(100001))
cum_x = [0] * 100001
cum_x[0] = 0
cum_x[1] = 1

for i in range(2, 100001):
    cum_x[i] = cum_x[i-1] + i
    
print(x[100000])
print(cum_x[100000])

s = int(input())