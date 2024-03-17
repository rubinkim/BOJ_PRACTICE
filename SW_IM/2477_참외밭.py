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
    if lst[i][0] in [3, 4]:
        if i == 0 and lst[i+1][0] == lst[5][0]:
            subtract_height = lst[i][1]
        elif 1 <= i <= 4 and lst[i-1][0] == lst[i+1][0]:
            subtract_height = lst[i][1]
        elif i == 5 and lst[i-4][0] == lst[0][0]:
            subtract_height = lst[i][1]

for i in range(6):
    if lst[i][0] in [1, 2]:
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


quant = int(input())
lst = []

for i in range(6):
    direction, length = map(int, input().split())
    lst.append((direction, length))
    
#print(lst)

max_height = max([lst[i][1] for i in range(6) if lst[i][0] in [3, 4]])
max_width = max([lst[i][1]  for i in range(6) if lst[i][0] in [1, 2]])
print(f"max_height : {max_height},  max_width : {max_width}")

no_max_height = [lst[i][1] for i in range(6) if lst[i][0] in [3, 4] and lst[i][1] != max_height]
no_max_width = [lst[i][1] for i in range(6) if lst[i][0] in [1, 2] and lst[i][1] != max_width]
print(f"no_max_height : {no_max_height},  no_max_width : {no_max_width}")

total_plantable_area = 0
max_area = max_height * max_width


i = 0
while i <= len(lst) - 1:
    if lst[i][0] == 1:    # ?ãú?ûë?ù¥ ?èôÏ™?(1) -> ?ã§?ùå Î∞©Ìñ•??? Î∂ÅÏ™Ω(4)
        if lst[i][1] == max_width:
            if lst[i+1][1] == max_height:
                total_plantable_area = max_area - lst[i+3][1] * lst[i+4][1]
            else:
                total_plantable_area = max_area - lst[i+2][1] * lst[i+3][1]
        else:
            if lst[i+1][1] == max_height:
                total_plantable_area = max_area - lst[i+4][1] * lst[i+5][1]
            else:
                total_plantable_area = max_area - lst[i+1][1] * lst[i+2][1]
                
    elif lst[i][0] == 2:    # ?ãú?ûë?ù¥ ?ÑúÏ™?(2) -> ?ã§?ùå Î∞©Ìñ•??? ?Ç®Ï™?(3)
        if lst[i][1] == max_width:
            if lst[i+1][1] == max_height:
                total_plantable_area = max_area - lst[i+3][1] * lst[i+4][1]
            else:
                total_plantable_area = max_area - lst[i+2][1] * lst[i+3][1]
        else:
            if lst[i+1][1] == max_height:
                total_plantable_area = max_area - lst[i+4][1] * lst[i+5][1]
            else:
                total_plantable_area = max_area - lst[i+1][1] * lst[i+2][1]
"""
"""
quant = int(input())
lst = []

for i in range(6):
    direction, length = map(int, input().split())
    lst.append((direction, length))
    
#print(lst)

max_height = max([lst[i][1] for i in range(6) if lst[i][0] in [3, 4]])
max_width = max([lst[i][1]  for i in range(6) if lst[i][0] in [1, 2]])
#print(f"max_height : {max_height},  max_width : {max_width}")

no_max_height = [lst[i][1] for i in range(6) if lst[i][0] in [3, 4] and lst[i][1] != max_height]
no_max_width = [lst[i][1] for i in range(6) if lst[i][0] in [1, 2] and lst[i][1] != max_width]
#print(f"no_max_height : {no_max_height},  no_max_width : {no_max_width}")

total_plantable_area = 0
max_area = max_height * max_width
                
def calculate_area(lst):
    global max_area
    
    if lst[0][0] in [1, 2]:    
        if lst[0][1] == max_width:
            if lst[1][1] == max_height:
                total_plantable_area = max_area - lst[3][1] * lst[4][1]
            else:
                total_plantable_area = max_area - lst[2][1] * lst[3][1]
        else:
            if lst[1][1] == max_height and lst[2][1] == max_width:
                total_plantable_area = max_area - lst[4][1] * lst[5][1]
            elif lst[1][1] == max_height and lst[2][1] != max_width:
                total_plantable_area = max_area - lst[3][1] * lst[4][1]                
                
            else:
                if lst[2][1] == max_width:
                    total_plantable_area = max_area - lst[5][1] * lst[0][1]
                else:
                    total_plantable_area = max_area - lst[1][1] * lst[2][1]                
                
    elif lst[0][0] in [3, 4]:    
        if lst[0][1] == max_height:
            if lst[1][1] == max_width:
                total_plantable_area = max_area - lst[3][1] * lst[4][1]
            else:
                total_plantable_area = max_area - lst[2][1] * lst[3][1]
        else:
            if lst[1][1] == max_width and lst[2][1] == max_height:
                total_plantable_area = max_area - lst[4][1] * lst[5][1]
            elif lst[1][1] == max_width and lst[2][1] != max_height:
                total_plantable_area = max_area - lst[3][1] * lst[4][1]
                
            else:
                if lst[2][1] == max_height:
                    total_plantable_area = max_area - lst[5][1] * lst[0][1]
                else:
                    total_plantable_area = max_area - lst[1][1] * lst[2][1]
                    
    return total_plantable_area

print(calculate_area(lst))
"""

quant = int(input())
lst = []

for i in range(6):
    direction, length = map(int, input().split())
    lst.append((direction, length))

max_height = max([lst[i][1] for i in range(6) if lst[i][0] in [3, 4]])
max_width = max([lst[i][1]  for i in range(6) if lst[i][0] in [1, 2]])

total_plantable_area = 0
max_area = max_height * max_width


print(calculate_area(lst))
                