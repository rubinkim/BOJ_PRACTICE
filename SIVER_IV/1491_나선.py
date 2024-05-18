#-*- coding: utf-8 -*-
"""
6 4
(1 2)

6 5
(3 2)

1 11
(0 10)

12 50
(5 6)

(5000 5000)
2499 2500
"""

n, m = map(int, input().split())    # n : number of columns,  m : number of rows
arr = [[0] * n for _ in range(m)]

for row in arr:
    print(row)