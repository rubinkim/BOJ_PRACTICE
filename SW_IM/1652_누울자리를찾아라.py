#-*- coding: utf-8 -*-
"""
5
....X
..XX.
.....
.XX..
X....
"""

n = int(input())
arr = [[0] * n for _ in range(n)]
for row in arr:
    print(row)
    
for i in range(n):
    for j in range(n):
        if arr[i][j] == '.':
            arr[i][j] = 0
        elif arr[i][j] == 'X':
            arr[i][j] = 1
            
for row in arr:
    print(row)
        