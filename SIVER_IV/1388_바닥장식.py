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
    for j in range(1, m):
        if arr[i][j-1] == arr[i][j] == '-':
            if j < m-1 and arr[i][j+1] == '|':
                cnt += 1
            if j == m-1:
                cnt += 1
        