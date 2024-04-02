#-*- coding: utf-8 -*-
"""
14

(2/4)
"""
dy = (1, -1, 0, 1)
dx = (0, 1, 1, -1)
y, x = 1, 1

n = int(input())
step = 0
dr = 0

while step <= n:
    if y == 1 and x == 1:
        dr = 0
    if y > 1 and y % 2 == 0 and x == 1:
        dr = 1
    if y == 0 and x > 1 and x % 2 == 0:
        dr = 2
    if y == 0 and x > 0 and x % 2 == 1:
        dr = 3
    if y > 1 and y % 2 == 1 and x == 0:
        dr = 0
    y = y + dy[dr]
    x = x + dx[dr]
    step += 1

    if step == n:
        print(str(y) + '/' + str(x))
        break