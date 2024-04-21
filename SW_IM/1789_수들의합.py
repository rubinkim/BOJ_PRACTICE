#-*- coding: utf-8 -*-
"""
200

19
"""
x = list(range(20))
cum_x = [0] * 100
cum_x[0] = 0
cum_x[1] = 1

for i in range(2, 100):
    cum_x[i] = cum_x[i-1] + i
    
print(x)
print(cum_x[:20])