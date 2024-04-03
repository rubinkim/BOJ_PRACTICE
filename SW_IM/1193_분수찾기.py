#-*- coding: utf-8 -*-
"""
14

(2/4)

# 시간 초과!!!

dy = (0, 1, 1, -1)
dx = (1, -1, 0, 1)
y, x = 1, 1

n = int(input())
step = 1
dr = 0

while step <= n:
    if step == n:
        print(str(y) + '/' + str(x))
        break
    
    if y == 1 and x == 1:
        dr = 0
    if x > 1 and x % 2 == 0 and y == 1:
        dr = 1
    if x == 1 and y > 1 and y % 2 == 0:
        dr = 2
    if x == 1 and y > 1 and y % 2 == 1:
        dr = 3
    if x > 1 and x % 2 == 1 and y == 1:
        dr = 0
    y = y + dy[dr]
    x = x + dx[dr]
    step += 1
"""
n = int(input())
lst = [1]
ans = (1, 1)
sum = 1
i = 2

while sum < n:
    
