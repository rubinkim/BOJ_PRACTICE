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
    row = input().split()
    for j in range(len(row)):
        arr[i][j] = row[j]
for row in arr:
    print(row)    
    
for i in range(n):
    row = input().split()
    for j in range(len(row)):
        if arr[i][j] == '.':
            arr[i][j] = 0
        elif arr[i][j] == 'X':
            arr[i][j] = 1
            
for row in arr:
    print(row)
        