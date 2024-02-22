#-*- coding: utf-8 -*-

"""
2
4 5
WRWRW
BWRWB
WRWRW
RWBWR
6 14
WWWWWWWWWWWWWW
WWRRWWBBBBBBWW
WRRRWWWBWWWWRB
WWBWBWWWBWRRRR
WBWBBWWWBBWRRW
WWWWWWWWWWWWWW
"""

TC = int(input())

N1, M1 = map(int, input().split())
arr1 = [[""] * M1 for _ in range(N1)]
for i in range(N1):
    for j, x in enumerate(input()):
        arr1[i][j] = x
        
N2, M2 = map(int, input().split())
arr2 = [[""] * M2 for _ in range(N2)]
for i in range(N2):
    for j, x in enumerate(input()):
        arr2[i][j] = x
        
print(TC)
print(N1, M1)
for row in arr1:
    print(row)
print(N2, M2)
for row in arr2:
    print(row)
    
cnt_lst = []    
for w in range(N1-3):
    cnt = 0
    for wj in range(M1):
        if arr1[w][wj] != 'W':
            cnt += 1
    for b in range(w+1, N1-2):
        for bj in range(M1):
            if arr1[b][bj] != 'B':
                cnt += 1
        for r in range(b+1, N1):
            for j in range(M1):
                if arr1[w][]