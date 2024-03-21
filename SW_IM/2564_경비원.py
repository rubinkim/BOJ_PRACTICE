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
    elif direction == 2:
        distance = h + distance
    elif direction == 3:
        distance = distance
    elif direction == 4:
        distance = h + w + (h - distance)
    lst.append((direction, distance))
        
print(lst)

total_dist = 0
my_location = lst[-1][1]
for i in range(N):
    if abs(my_location - lst[i][1]) > w + h:
        