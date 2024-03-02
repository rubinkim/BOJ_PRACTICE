#-*- coding: utf-8 -*-

"""
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
"""

bingo = []
calls = []


for i in range(10):    
    if i < 5:
        bingo.append(list(map(int, input().split())))
    else:
        calls.extend(list(map(int, input().split())))        
        
for row in bingo:
    print(row)
print()
print(calls)

for i in range(len(calls)):
    for j in range(5):
        for k in range(5):
    