#-*- coding: utf-8 -*-
"""
3
2 2
1 5
13 29

(1 5 67863915)
"""

from math import factorial
import time

start = time.time()
tc = int(input())
for _ in range(tc):
    n, m = map(int, input().split())
    ans = int(factorial(m) / (factorial(m-n) * factorial(n)))
    print(ans)
end = time.time()
print(f"lapse : {end - start}")