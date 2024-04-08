#-*- coding: utf-8 -*-
"""
25 7 5

(2)
"""
import math
a, b, n = map(int, input().split())
print(f"a : {a}, b : {b}, n : {n}")

print(f"a/b : {a * 10**n / b}")
ln_ans = math.log(a * 10 ** n / b)
print(f"ln_ans : {ln_ans}")
ans = math.exp(ln_ans)
print(f"ans : {ans}")