#-*- coding: utf-8 -*-
"""
0 0 0 1 1 0
(0.8284271247461898)

0 0 4 0 0 3
(4.0)

0 0 1 0 47 0
(-1.0)

1 2 3 4 8 7
(11.547796284592874)

2 -1 -7 2 -1 0
(-1.0)
"""
x_a, y_a, x_b, y_b, x_c, y_c = map(int, input().split())
print(f"{(x_a, y_a), (x_b, y_b), (x_c, y_c)}")

def calc_distance(x1, y1, x2, y2):
    dist = (abs(x2 - x1) ** 2 + abs(y2 - y1) ** 2) ** 0.5
    return dist

dist_ab = calc_distance(x_a, y_a, x_b, y_b)
dist_bc = calc_distance(x_b, y_b, x_c, y_c)
dist_ca = calc_distance(x_c, y_c, x_a, y_a)