#-*- coding: utf-8 -*-
"""
7
4 50
2 160
3 30
1 60
3 20
1 100

47600

quant = int(input())
lst = []

for i in range(6):
    direction, length = map(int, input().split())
    lst.append((direction, length))

max_height = max([lst[i][1] for i in range(6) if lst[i][0] in [3, 4]])
max_width = max([lst[i][1]  for i in range(6) if lst[i][0] in [1, 2]])

def calculate_area(lst):
    global max_height, max_width
    max_area = max_height * max_width
    
    if lst[0][0] in [1, 2]:
        if lst[0][1] == max_width:
            if lst[1][1] == max_height:
                plant_area = max_area - lst[3][1] * lst[4][1]
            else:
                plant_area = max_area - lst[2][1] * lst[3][1]
        else:
            if lst[1][1] == max_height:
                plant_area = max_area - lst[4][1] * lst[5][1]
            else:
                plant_area = max_area - lst[1][1] * lst[2][1]
                
    elif lst[0][0] in [3, 4]:
        if lst[0][1] == max_height:
            if lst[1][1] == max_width:
                plant_area = max_area - lst[3][1] * lst[4][1]
            else:
                plant_area = max_area - lst[2][1] * lst[3][1]
        else:
            if lst[1][1] == max_width:
                plant_area = max_area - lst[4][1] * lst[5][1]
            else:
                plant_area = max_area - lst[1][1] * lst[2][1]
    return plant_area

print(quant * calculate_area(lst))
"""                

quant = int(input())
lst = []

for i in range(6):
    direction, length = map(int, input().split())
    lst.append((direction, length))

max_height = max([lst[i][1] for i in range(6) if lst[i][0] in [3, 4]])
max_width = max([lst[i][1]  for i in range(6) if lst[i][0] in [1, 2]])

for i in range(6):
    if lst[i][0] in [1, 2] and lst[i][1] == max_width:
        max_width_idx = i
    if lst[i][0] in [3, 4] and lst[i][1] == max_height:
        max_height_idx = i

print(f"lst : {lst}")
print(f"max_width_idx : {max_width_idx},  max_width : {max_width}")
print(f"max_height_idx : {max_height_idx},  max_height : {max_height}")