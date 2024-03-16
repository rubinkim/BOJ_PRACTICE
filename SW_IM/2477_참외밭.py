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

max_height = max([(lst[i][1]) for i in range(6) if lst[i][0] in [3, 4]])
max_width = max([(lst[i][1]  for i in range(6) if lst[i][0] in [1, 2])])
print(f"max_height : {max_height},  max_width : {max_width}")
