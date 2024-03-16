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
"""
quant = int(input())
lst = []

for i in range(6):
    direction, length = map(int, input().split())
    lst.append((direction, length))
    
print(lst)

max_height = max([lst[i][1] for i in range(6) if lst[i][0] in [3, 4]])
max_width = max([lst[i][1]  for i in range(6) if lst[i][0] in [1, 2]])
#print(f"max_height : {max_height},  max_width : {max_width}")

subtract_height = 0
subtract_width = 0

for i in range(6):
    if lst[i][0] == 3 or lst[i][0] == 4:
        if i == 0 and lst[i+1][0] == lst[5][0]:
            subtract_height = lst[i][1]
        elif 1 <= i <= 4 and lst[i-1][0] == lst[i+1][0]:
            subtract_height = lst[i][1]
        elif i == 5 and lst[i-4][0] == lst[0][0]:
            subtract_height = lst[i][1]

for i in range(6):
    if lst[i][0] == 1 or lst[i][0] == 2:
        if i == 0 and lst[i+1][0] == lst[5][0]:
            subtract_width = lst[i][1]
        elif 1 <= i <= 4 and lst[i-1][0] == lst[i+1][0]:
            if lst[i-1][0] == lst[i+1][0]:
                subtract_width = lst[i][1]
        elif i == 5 and lst[i-1][0] == lst[0][0]:
            subtract_width = lst[i][1]
                
#print(f"subtract_height : {subtract_height},  subtract_width : {subtract_width}")

plantable_area = max_height * max_width - subtract_height * subtract_width
total_product = quant * plantable_area
print(total_product)
        