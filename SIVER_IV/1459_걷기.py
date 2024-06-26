#-*- coding: utf-8 -*-
"""
4 2 3 10
(18)

4 2 3 5
(16)

2 0 12 10
(20, 24)

25 18 7 11
(247, 247)

24 16 12 10
(240, 256)

10000000 50000000 800 901
(41010000000, 41010000000)

135 122 43 29
(3929, 4097)
"""

x, y, w, s = map(int, input().split())
#print(f"x : {x},  y : {y},  w : {w},  s : {s}")

dist = 0
if s <= w:
    if abs(x-y) % 2 == 0:
        dist = max(x, y) * s
    else:
        dist = min(x, y) * s + (abs(x-y) - 1) * s + w
elif w < s <= 2*w:
    dist = min(x, y) * s + abs(x-y) * w
elif s > 2*w:
    dist = (x + y) * w

print(dist)