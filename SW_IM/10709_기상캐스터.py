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
joi = []
for _ in range(H):
    joi.append(" ".join(input()))
    
for row in joi:
    print(row)

print(joi)