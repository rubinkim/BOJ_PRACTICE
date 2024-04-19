#-*- coding: utf-8 -*-
"""
5
....X
..XX.
.....
.XX..
X....

(5 4)
"""

n = int(input())
arr = [[0] * n for _ in range(n)]

for i in range(len(arr)):
    row = input()
    for j in range(len(row)):
        arr[i][j] = row[j]
    
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
    
col_cnt, row_cnt = 0, 0

for i in range(len(arr)):
    if any([sum(arr[i][j:j+2]) == 0 for j in range(len(arr[i])-1)]) and sum(arr[i]) >= 1:
        col_cnt += 1
    if i == 0 and sum(arr[i]) == 0 and sum(arr[i+1]) >= 1:
        col_cnt += 1
    if i == n-1 and sum(arr[i]) == 0 and sum(arr[i-1]) >= 1:
        col_cnt += 1
    if 1 <= i <= i-2 and sum(arr[i]) == 0 and (sum(arr[i-1]) >= 1 or sum(arr[i+1]) >= 1):
        col_cnt += 1
        
for i in range(len(arr)):
    print(sum(arr[i]))