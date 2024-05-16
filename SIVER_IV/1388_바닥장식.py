#-*- coding: utf-8 -*-
"""
4 4
----
----
----
----
(4)

6 9
-||--||--
--||--||-
|--||--||
||--||--|
-||--||--
--||--||-
(31)

7 8
--------
|------|
||----||
|||--|||
||----||
|------|
--------
(13)

10 10
||-||-|||-
||--||||||
-|-|||||||
-|-||-||-|
||--|-||||
||||||-||-
|-||||||||
||||||||||
||---|--||
-||-||||||
(41)

6 6
-||--|
||||||
|||-|-
-||||-
||||-|
||-||-
(19)
"""
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(input())
 
for row in arr:
    print(row)
    
arr_transpose = list(map(list, zip(*arr)))
for row in arr_transpose:
    print(row)
    
cnt = 0

for i in range(n):
    for j in range(m):
        if j == 0:
            if arr[i][j] == '-' and arr[i][j+1] == '|':
                cnt += 1
        if 1 <= j <= m-2:
            if arr[i][j-1] == '|' and arr[i][j] == '-' and arr[i][j+1] == '|':
                cnt += 1
        if j == m-1:
            if arr[i][j-1] == '|' and arr[i][j] == '-':
                cnt += 1

for i in range(n):
    for j in range(1, m):            
        if arr[i][j-1] == arr[i][j] == '-':
            if j < m-1 and arr[i][j+1] == '|':
                cnt += 1
            if j == m-1:
                cnt += 1

for i in range(m):
    for j in range(1, n):
        if arr_transpose[i][j-1] == arr_transpose[i][j] == '|':
            if j < n-1 and arr_transpose[i][j+1] == '-':
                cnt += 1
            if j == n-1:
                cnt += 1
                
for i in range(m):
    for j in range(n):
        if j == 0:
            if arr_transpose[i][j] == '|' and arr_transpose[i][j+1] == '-':
                cnt += 1
        if 1 <= j <= n-2:
            if arr_transpose[i][j-1] == '-' and arr_transpose[i][j] == '|' and arr_transpose[i][j+1] == '-':
                cnt += 1
        if j == n-1:
            if arr_transpose[i][j-1] == '-' and arr[i][j] == '-':
                cnt += 1
                
print(cnt)               

        