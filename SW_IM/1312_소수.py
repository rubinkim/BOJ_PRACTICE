#-*- coding: utf-8 -*-
"""
25 7 5

(2)
"""

a, b, n = map(int, input().split())
#print(f"a : {a}, b : {b}, n : {n}")

#print(f"a/b : {a * 10**n / b}")
ans = str(a * 10 ** n / b)[:n+1][-1]
print()