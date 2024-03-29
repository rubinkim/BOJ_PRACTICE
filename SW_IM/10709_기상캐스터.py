#-*- coding: utf-8 -*-
"""
3 4
c..c
..c.
....

0 1 2 0
-1 -1 0 1
-1 -1 -1 -1


6 8
.c......
........
.ccc..c.
....c...
..c.cc..
....c...

-1 0 1 2 3 4 5 6
-1 -1 -1 -1 -1 -1 -1 -1
-1 0 0 0 1 2 0 1
-1 -1 -1 -1 0 1 2 3
-1 -1 0 1 0 0 1 2
-1 -1 -1 -1 0 1 2 3
"""

H, W = map(int, input().split())
arr = [input() for _ in range(H)]
v = [[0] * W for _ in range(H)]

for i in range(H):
    cnt = -1
    for j in range(W):
        if arr[i][j] == 'c':
            cnt = 0
        else:
            if cnt >= 0:
                cnt += 1
        v[i][j] = cnt

for lst in v:
    print(*lst)
