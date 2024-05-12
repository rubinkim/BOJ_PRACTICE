#-*- coding: utf-8 -*-
"""
3 5
1 2 4
2 3 4 5 6

(4)
"""
len_a, len_b = map(int, input().split())
a = set(map(int, input().split()))
b = set(map(int, input().split()))
print(f"a : {a},  b : {b}")

not_a = a - b
not_b = b - a
print(f"not_a : {not_a},  not_b : {not_b}")
