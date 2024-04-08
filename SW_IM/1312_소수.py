#-*- coding: utf-8 -*-
"""
25 7 5

(2)
"""

a, b, n = map(int, input().split())
print(f"a : {a}, b : {b}, n : {n}")

print(f"a/b : {a * 10**n / b}")
print(str(a * 10 ** n / b).rstrip('\[.0-9]+'))