#-*- coding: utf-8 -*-

"""
4
3 7
5 2
15 7
13 14

96
"""

N = int(input())
arr = [[0] * 102 for _ in range(102)]
for _ in range(N):
    sj, si = map(int, input().split())
    for i in range(si, si+10):
        for j in range(sj, sj+10):
            arr[i][j] = 1

def count(arr):
    pass

arr_t = list(zip(*arr))
