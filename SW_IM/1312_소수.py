#-*- coding: utf-8 -*-
"""
25 7 5

(2)
"""
a, b, n = map(int, input().split())
print(f"a : {a},  b : {b},  n : {n}")
print(f"a/b : {a/b}")
print()

a %= b
print(f"a : {a}")
print()

for i in range(n-1):
    a = (a*10) % b
    print(f"a : {a}")

print((a*10) // b)