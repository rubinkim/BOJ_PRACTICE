#-*- coding: utf-8 -*-
"""
14

(2/4)

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
    sum += i
    lst.append(sum)
    i += 1

#print(lst)
if len(lst) == 1:
    ans = (1, 1)
else:
    leftover = n - lst[-2]
    if len(lst) % 2 == 1:
        start = (len(lst), 1)
        ans = (len(lst)-leftover+1, leftover)
    elif len(lst) % 2 == 0:
        start = (1, len(lst))
        ans = (leftover, len(lst)-leftover+1)

print(str(ans[0]) + '/' + str(ans[1]))