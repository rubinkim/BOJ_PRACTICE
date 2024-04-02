#-*- coding: utf-8 -*-
"""
14

(2/4)
"""
dy = {1, -1, 0, 1}
dx = {0, 1, 1, -1}
y, x = 0, 0

n = int(input())
step = 0
while step <= n:
    if step == n:
        print(str(y+1) + '/' + str(x+1))
        break
    