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
n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(input())
print()
for row in arr:
    print(row)
print()    
arr_transpose = list(map(list, zip(*arr)))
for row in arr_transpose:
    print(row)

cnt = 0
if n == 1 and m == 1:
    cnt += 1
    
elif n == 1 and m >= 2:
    for j in range(m):
        if j == 0:            
            if arr[0][j] == '-' and arr[0][j+1] == '|':
                cnt += 1
        elif 1 <= j <= m-2:
            print(f"arr[j-1] : {arr[j-1]}")
            print(f"arr[j] : {arr[j]}")
            print(f"arr[j+1] : {arr[j+1]}")
            if arr[0][j-1] == '|' and arr[0][j] == '-' and arr[0][j+1] == '|':
                cnt += 1
        elif j == m-1:
            if arr[0][j-1] == '|' and arr[0][j] == '-':
                cnt += 1
                
    for j in range(1, m):
        if arr[0][j-1] == arr[0][j] == '-':
            if j < m-1 and arr[0][j+1] == '|':
                cnt += 1
            if j == m-1:
                cnt += 1
                
elif m == 1 and n >= 2:
    for j in range(n):
        if j == 0:
            if arr_transpose[j] == '|' and arr_transpose[j+1] == '-':
                cnt += 1
        if 1 <= j <= n-2:
            if arr_transpose[j-1] == '-' and arr_transpose[j] == '|' and arr_transpose[j+1] == '-':
                cnt += 1
        if j == n-1:
            if arr_transpose[j-1] == '-' and arr_transpose[j] == '|':
                cnt += 1
                
    for j in range(1, n):
        if arr_transpose[j-1] == arr_transpose[j] == '|':
            if j < n-1 and arr[0][j+1] == '-':
                cnt += 1
            if j == n-1:
                cnt += 1

elif n >= 2 and m >= 2:
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
        for j in range(n):
            if j == 0:
                if arr_transpose[i][j] == '|' and arr_transpose[i][j+1] == '-':
                    cnt += 1
            if 1 <= j <= n-2:
                if arr_transpose[i][j-1] == '-' and arr_transpose[i][j] == '|' and arr_transpose[i][j+1] == '-':
                    cnt += 1
            if j == n-1:
                if arr_transpose[i][j-1] == '-' and arr_transpose[i][j] == '|':
                    cnt += 1
                    
    for i in range(m):
        for j in range(1, n):
            if arr_transpose[i][j-1] == arr_transpose[i][j] == '|':
                if j < n-1 and arr_transpose[i][j+1] == '-':
                    cnt += 1
                if j == n-1:
                    cnt += 1


                
print(cnt)               

        