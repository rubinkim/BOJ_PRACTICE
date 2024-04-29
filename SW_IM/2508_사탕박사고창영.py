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
    for i in range(r):
        for j in range(c):
            if ord(box[i][j]) == 111:
                if (1 <= i <= r-1) and (ord(box[i-1][j]) == 118 and ord(box[i+1][j]) == 94):
                    cnt += 1
                if (1 <= j <= c-1) and (ord(box[i][j-1]) == 62 and ord(box[i][j+1]) == 60):
                    cnt += 1
    print(cnt)