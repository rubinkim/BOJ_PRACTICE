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