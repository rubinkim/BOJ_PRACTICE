#-*- coding: utf-8 -*-
"""
20 10 5 0 3
15 5
1 5
1 1

(2)


20 10 0 0 14
-5 5
-4 2
-4 8
-3 1
-3 9
0 0
0 10
20 0
20 10
23 1
23 9
24 2
24 8
25 5

(14)


52 84 -44 66 10
26 118
-33 106
-49 128
40 114
-10 101
47 85
25 142
-16 140
-82 126
7 145

(8)


24 100 -62 71 8
-63 109
-26 164
-9 91
-113 80
-124 75
-95 140
-89 116
-55 113

(6)
"""
w, h, x, y, p = map(int, input().split())
r = h / 2
cnt = 0

for _ in range(p):
    coord_x, coord_y = map(int, input().split())
    if (x <= coord_x <= x+w) and (y <= coord_y <= y+h):
        cnt += 1
    else:
        if ((x - coord_x) ** 2 + (y+r - coord_y) ** 2) ** 0.5 <= r:
            cnt += 1
        elif ((coord_x - (x+w)) ** 2 + (coord_y - (y+r)) ** 2) ** 0.5 <= r:
            cnt += 1
print(cnt)