#-*- coding: utf-8 -*-
"""
200

19
"""
x = list(range(1, 20))
cum_x = [1] * 10001
for i in range(2, 100):
    cum_x[i] += i
print(x)
print(cum_x[:20])