#-*- coding: utf-8 -*-
"""
4 2
12 3
15 4
(12)

10 3
20 8
40 7
60 4
(36)

15 1
100 40
(300)

17 1
12 3
(36)

7 2
10 3
12 2
(12)

9 16
21 25
77 23
23 88
95 43
96 19
59 36
80 13
51 24
15 8
25 61
21 22
3 9
68 68
67 100
83 98
96 57
(6)
"""

n, m = map(int, input().split())
lst_pack, lst_piece = [], []

for _ in range(m):
    a, b = map(int, input().split())
    lst_pack.append(a/6)
    lst_piece.append(b)
    
min_pack = min(lst_pack)
min_piece = min(lst_piece)
    
min_val = 0
