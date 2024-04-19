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

for i in range(len(arr)):
    row = input()
    for j in range(len(row)):
        arr[i][j] = row[j]
for row in arr:
    print(row)    
    
for i in range(n):
    for j in range(len(row)):
        if arr[i][j] == '.':
            arr[i][j] = 0
        elif arr[i][j] == 'X':
            arr[i][j] = 1
            
for row in arr:
    print(row)
    
print()

arr_tr = list(zip(*arr))
for row in arr_tr:
    print(row)
        