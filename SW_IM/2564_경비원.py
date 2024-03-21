#-*- coding: utf-8 -*-
"""
10 5
3
1 4
3 2
2 8
2 3

23
"""

w, h = map(int, input().split())
N = int(input())
lst = []

# direction : 1(north), 2(south), 3(west), 4(east)
for _ in range(N+1):
    direction, distance = map(int, input().split())
    if direction == 1:
        distance = h + w + h + (w - distance)
    