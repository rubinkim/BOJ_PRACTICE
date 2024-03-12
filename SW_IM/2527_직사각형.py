#-*- coding: utf-8 -*-
"""
3 10 50 60 100 100 200 300
45 50 600 600 400 450 500 543
11 120 120 230 50 40 60 440
35 56 67 90 67 80 500 600
"""

for _ in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, input().split())
    print(f"x1 : {x1}, y1 : {y1}, p1 : {p1}, q1 : {q1}, x2 : {x2}, y2 : {y2}, p2 : {p2}, q2 : {q2}")

    small_x = min(x1, x2)
    small_y = min(y1, y2)
    large_x = max(p1, p2)
    large_y = max(q1, q2)

    print(f"small_x : {small_x}, small_y : {small_y}, large_x : {large_x}, large_y : {large_y}")

    if (large_x - small_x) < (p1 - x1) + (p2 - x2) and (large_y - small_y) < (q1 - y1) + (q2 - y2):
        print("a")
    elif ((large_x - small_x) == (p1 - x1) + (p2 - x2) and (large_y - small_y) < (q1 - y1) + (q2 - y2)) or ((large_x - small_x) < (p1 - x1) + (p2 - x2) and (large_y - small_y) == (q1 - y1) + (q2 - y2)):
        print("b")
    elif (large_x - small_x) == (p1 - x1) + (p2 - x2) and (large_y - small_y) == (q1 - y1) + (q2 - y2):
        print("c")
    elif (large_x - small_x) > (p1 - x1) + (p2 - x2) and (large_y - small_y) > (q1 - y1) + (q2 - y2):
        print("d")