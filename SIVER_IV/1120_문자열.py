#-*- coding: utf-8 -*-
"""
adaabc aababbc
(2)

hello xello
(1)

koder topcoder
(1)

abc topabcoder
(0)

giorgi igroig
(6)
"""

a, b = input().split()
print(f"a : {a},  b : {b}")

diff = len(b) - len(a)
print(f"diff : {diff}")