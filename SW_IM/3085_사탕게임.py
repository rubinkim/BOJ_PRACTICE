#-*- coding: utf-8 -*-
"""
3
CCP
CCP
PPC

3


4
PPPP
CYZY
CCPY
PPCC

4


5
YCPZY
CYZZP
CCPPP
YCYZC
CPPZZ

4
"""
N = int(input())
lst = [list(input()) for _ in range(N)]
lst_t = [[""] * N for _ in range(N)]

for i in range(N):
    for j in range(N):
        lst_t[i][j] = lst[j][i]

for row in lst:
    print(row)
    
print()

for row in lst_t:
    print(row)

cnt = 0    
for i in range(N):
    for j in range(N-1):
        if lst[i][j] != lst[i][j+1]:
            lst[i][j], lst[i][j+1] = lst[i][j+1], lst[i][j]
            
