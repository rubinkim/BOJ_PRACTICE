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

start_time_lst = []
interval_lst = []
num_bus_lst = []

for _ in range(n):
    s, i, c = map(int, input().split())
    start_time_lst.append(s)
    interval_lst.append(i)
    num_bus_lst.append(c)
    
print(f"n : {n},  t : {t}")
print(f"start_time_lst : {start_time_lst}")
print(f"interval_lst : {interval_lst}")
print(f"num_bus_lst : {num_bus_lst}")
