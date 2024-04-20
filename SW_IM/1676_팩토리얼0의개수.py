#-*- coding: utf-8 -*-
"""
10

(2)

3

(0)
"""

n = int(input())
cache = [0] * (n+1)

def cal_factorial(x):
    if x <= 1:
        return 1
    else:
        cache[x] = x * cal_factorial(x-1)
        return cache[x]

ans = 0
my_fac = cal_factorial(n)
print(my_fac)

if my_fac % 10 != 0:
    print(ans)
else:
    i = 0
    while my_fac % (10 ** i) == 0:
        ans += 1
        i += 1
    print(ans-1)