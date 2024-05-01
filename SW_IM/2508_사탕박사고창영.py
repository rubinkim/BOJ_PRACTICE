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

tc = int(input())

for _ in range(tc):
    input()
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
"""
tc = int(input())

for _ in range(tc):
    input()    
    r, c = map(int, input().split())
    box = [[] for _ in range(r)]
    for i in range(r):
        box[i] = input()
    
    cnt = 0
    
    if r <= 2 and c <= 2:
        cnt = 0
        
    elif r == 1 and c >= 3:
        for j in range(1, c-1):
            if ord(box[0][j-1]) == 62 and ord(box[0][j]) == 111 and ord(box[0][j+1]) == 60:
                cnt = 1
    elif r == 2 and c >= 3:
        for j in range(1, c-1):
            if ord(box[0][j-1]) == 62 and ord(box[0][j]) == 111 and ord(box[0][j+1]) == 60:
                cnt = 1
            if ord(box[1][j-1]) == 62 and ord(box[1][j]) == 111 and ord(box[1][j+1]) == 60:
                cnt = 1
                
    elif r >= 3 and c == 1:
        for i in range(1, r-1):                                                                           
            if ord(box[i-1][0]) == 118 and ord(box[i][0]) == 111 and ord(box[i+1][0]) == 94:
                cnt = 1
    elif r >=3 and c == 2:                                                                                   
        for i in range(1, r-1):                                                                          
            if ord(box[i-1][0]) == 118 and ord(box[i][0]) == 111 and ord(box[i+1][0]) == 94:
                cnt = 1
            if ord(box[i-1][1]) == 118 and ord(box[i][1]) == 111 and ord(box[i+1][1]) == 94:
                cnt = 1
                    
    if r >= 3 and c >= 3:
        for i in range(r):
            for j in range(c):
                if (i == 0 or i == r-1) and (1 <= j <= c-1) and ord(box[i][j-1]) == 62 and ord(box[i][j]) == 111 and ord(box[i][j+1]) == 60:
                    cnt += 1
                if (1 <= i <= r-1) and (j == 0 or j == c-1) and ord(box[i-1][j]) == 118 and ord(box[i][j]) == 111 and ord(box[i+1][j]) == 94:
                    cnt += 1
                if (1 <= i <= r-1) and (1 <= j <= c-2) and ord(box[i-1][j]) == 118 and ord(box[i][j]) == 111 and ord(box[i+1][j]) == 94:
                    cnt += 1
                if (1 <= i <= r-2) and (1 <= j <= c-1) and ord(box[i][j-1]) == 62 and ord(box[i][j]) == 111 and ord(box[i][j+1]) == 60:
                    cnt += 1
    print(cnt)