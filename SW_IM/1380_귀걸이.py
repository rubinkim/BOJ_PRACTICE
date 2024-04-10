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

n = 200
scenario_num = 1
while n > 0: 
    n = int(input())
    if n == 0:
        break
        
    name_dict = {}
    for i in range(n):
        name_dict[i+1] = [input()]
    for _ in range(n):
        num, ch = input().split()
        num = int(num)
        name_dict[num].append(ch)
    #print(name_dict)
    for _ in range(n-1):
        num, ch = input().split()
        num = int(num)
        if ch != name_dict[num][1]:
            del name_dict[num]
    print(f"{scenario_num} {list(name_dict.values())[0][0]}")
    scenario_num += 1

            

        
    
    
