#-*- coding: utf-8 -*-
"""
1

5 4
.>o<
v.^.
ooo.
^.^.
>o<<

(3)
"""
tc = int(input())
input()

for _ in range(tc):
    r, c = map(int, input().split())
    box = [[] for _ in range(r)]
    for i in range(r):
        box[i] = input()
    
    cnt = 0
    for i in range(1, r-1):
        for j in range(1, c-1):
            if ord(box[i][j]) == 111:
                if (ord(box[i-1][j]) == 118 and ord(box[i+1][j]) == 94) or (ord(box[i][j-1]) == 62 and ord(box[i][j+1]) == 60):