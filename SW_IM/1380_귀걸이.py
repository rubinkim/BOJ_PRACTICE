#-*- coding: utf-8 -*-
"""
3
Betty Boolean
Alison Addaway
Carrie Carryon
1 B
2 A
3 B
3 A
1 A
2
Helen Clark
Margaret Thatcher
1 B
2 B
2 A
0

# answer
1 Alison Addaway
2 Helen Clark
"""

n = -1
while n == 0:
    n = int(input())
    if n == 0:
        break
    name_dict = {}
    for i in range(n):
        name_dict[i+1] = [input()]
    for _ in range(n):
        num, ch = input().split()
        name_dict[num].append(ch)
print(name_dict)
        
    
    
