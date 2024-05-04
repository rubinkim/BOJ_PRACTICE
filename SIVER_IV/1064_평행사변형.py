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

def calc_distance((x1, y1), (x2, y2)):