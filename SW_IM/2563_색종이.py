#-*- coding: utf-8 -*-

"""
3
3 7
15 7
5 2

260
"""

N = int(input())
arr = [[0] * 102 for _ in range(30)]
ans = 0

for _ in range(N):
    sj, si = map(int, input().split())      # sj : column,  si : row
    for i in range(si, si+10):
        for j in range(sj, sj+10):
            arr[i][j] = 1
            
for row in arr:
    print(row)