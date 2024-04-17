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
    if ((year - 1) * 15 + e) % 15 == e and ((year - 1) * 28 + s) % 28 == s and ((year - 1) * 19 + m) % 19 == m:
        print(year)
        break    
