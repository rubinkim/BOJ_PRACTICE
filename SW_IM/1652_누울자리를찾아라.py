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
            
arr_tr = list(map(list, zip(*arr)))
    
col_cnt, mtt = 0, 0
for i in range(n):
    j = 0
    while j < n:
        if j < n-1 and arr[i][j] == 0:
            mtt += 1
        elif j == n-1 and arr[i][j] == 0:
            if mtt >= 1 and sum(arr[i]) == 0:
                col_cnt += 1
          
        if arr[i][j] == 1:
            if mtt >= 2:
                col_cnt += 1
                mtt = 0
            else:
                mtt = 0   
        j += 1
    mtt = 0

for i in range(n):
    if i == 0 and sum(arr[i]) == 0 and sum(arr[i+1]) >= 1:
        col_cnt += 1
    if 1 <= i <= n-2 and sum(arr[i]) == 0 and (sum(arr[i-1]) >= 1 or sum(arr[i+1]) >= 1):
        col_cnt += 1
    if i == n-1 and sum(arr[i]) == 0 and sum(arr[i-1]) >= 1:
        col_cnt += 1
     
row_cnt, mtt = 0, 0
for i in range(n):
    j = 0
    while j < n:
        if j < n-1 and arr_tr[i][j] == 0:
            mtt += 1
        elif j == n-1 and arr_tr[i][j] == 0:
            if mtt >= 1 and sum(arr_tr[i]) == 0:
                row_cnt += 1
             
        if arr_tr[i][j] == 1:
            if mtt >= 2:
                row_cnt += 1
                mtt = 0
            else:
                mtt = 0   
        j += 1
    mtt = 0

for i in range(n):
    if i == 0 and sum(arr_tr[i]) == 0 and sum(arr_tr[i+1]) >= 1:
        row_cnt += 1
    if 1 <= i <= n-2 and sum(arr_tr[i]) == 0 and (sum(arr_tr[i-1]) >= 1 or sum(arr_tr[i+1]) >= 1):
        row_cnt += 1
    if i == n-1 and sum(arr_tr[i]) == 0 and sum(arr_tr[i-1]) >= 1:
        row_cnt += 1         
    
print(col_cnt, row_cnt)