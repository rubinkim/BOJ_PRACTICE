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

5 1
-
|
|
-
-
(3)


1 5
|--|-
(4)
"""
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(list(input()))
    
for row in arr:
    print(row)
    
def dfs(row, col):
    if arr[row][col] == '-':
        for j in [-1, 1]:
            adj_col = col + j
            if 0 < adj_col < m and arr[row][adj_col] == '-':
                dfs(row, adj_col)
    if arr[row][col] == '|':
        for i in [-1, 1]:
            adj_row = row + i
            if 0 < adj_row < n and arr[adj_row][col] == '|':
                dfs(adj_row, col)
                
for i in range(n):
    for j in range(m):
        if arr[i][j] == '-' or arr[i][j] == '|':
            dfs(i, j)
            count += 1