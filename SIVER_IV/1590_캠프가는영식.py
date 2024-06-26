#-*- coding: utf-8 -*-
"""
1 285
150 50 10
(15)

1 123456
123456 10000 1
(0)

3 1
270758 196 67
904526 8930 66
121164 3160 56
(121163)

3 1000000
718571 2557 74
480573 9706 54
16511 6660 90
(-1)

5 395439
407917 8774 24
331425 4386 58
502205 9420 32
591461 1548 79
504695 8047 53
(1776)
"""
n, t = map(int, input().split())

bus_info = {}
for idx in range(n):
    lst = []
    s, i, c = map(int, input().split())
    for j in range(c):
        lst.append(s + j * i)
    bus_info[idx] = lst
    
total_lst = []
for v in bus_info.values():
    total_lst.extend(v)
    
total_lst.sort()
#print(len(total_lst))

for x in total_lst:
    if t <= x:
        print(x-t)
        break
else:
    print(-1)