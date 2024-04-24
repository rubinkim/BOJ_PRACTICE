#-*- coding: utf-8 -*-
"""
5
1....
..3..
.....
.4...
...9.


*4330
14*30
47730
4*M99
44M*9
"""
n = int(input())
arr = [[0] * n for _ in range(n)]
for i in range(n):
    row = input()
    for j in range(len(row)):
        arr[i][j] = row[j]
    
arr = [["."] * (n+2)] + [["."] + arr[i] + ["."] for i in range(n)] + [["."] * (n+2)]
str_nums = list(map(str, range(1, 10)))

for i in range(len(arr)):
    for j in range(len(arr[i])):
        if arr[i][j] == ".":
            arr[i][j] = 0
        elif arr[i][j] in str_nums:
            arr[i][j] = int(arr[i][j])
    
for row in arr:
    print(row)
    
mines = [[0] * (n+2) for _ in range(n+2)]