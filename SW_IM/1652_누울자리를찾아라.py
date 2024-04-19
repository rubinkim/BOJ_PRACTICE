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

arr_tr = list(map(list, zip(*arr)))
    
for row in arr_tr:
    print(row)
    
col_cnt, mtt = 0, 0
for i in range(n):
    j = 0
    
    
row_cnt = 0
for i in range(len(arr_tr)):
    if any([sum(arr_tr[i][j:j+2]) == 0 for j in range(len(arr_tr[i])-1)]) and sum(arr_tr[i]) >= 1:
        row_cnt += 1
    if i == 0 and sum(arr_tr[i]) == 0 and sum(arr_tr[i+1]) >= 1:
        row_cnt += 1
    if i == n-1 and sum(arr_tr[i]) == 0 and sum(arr_tr[i-1]) >= 1:
        row_cnt += 1
    if 1 <= i <= n-2 and sum(arr_tr[i]) == 0 and (sum(arr_tr[i-1]) >= 1 or sum(arr_tr[i+1]) >= 1):
        row_cnt += 1    

print(col_cnt, row_cnt)