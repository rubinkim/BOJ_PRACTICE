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

for row in lst:
    print(row)