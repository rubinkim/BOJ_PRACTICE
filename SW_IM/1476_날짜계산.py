#-*- coding: utf-8 -*-
"""
1 16 16
(16)

1 1 1
(1)

1 2 3
(5266)

15 28 19
(7980)
"""

e, s, m = map(int, input().split())
year = 1

while True:
    if e == 15:
        e = 0
    if s == 28:
        s = 0
    if m == 19:
        m = 0
    if year % 15 == e and year % 28 == s and year % 19 == m:
        print(year)
        break
    year += 1
