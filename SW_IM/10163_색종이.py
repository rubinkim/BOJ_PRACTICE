#-*- coding: utf-8 -*-

"""
2
0 0 10 10
2 2 6 6

64 36


3
0 2 10 10
7 9 8 4
8 4 10 6

81 25 60


4
0 2 10 10
7 9 8 4
8 4 10 6
6 0 12 10

62 24 0 120
"""

N = int(input())
arr = [[0] * 20 for _ in range(20)]

for num in range(1, N+1):
    sj, si, w, h = map(int, input().split())
    for i in range(si, si+h):
        for j in range(sj, sj+w):
            arr[i][j] = num
            
for row in arr:
    print(row)
    
nums_lst = []

for x in range(1, N+1):
    cnt = 0
    for i in range(20):
        for j in range(20):
            if arr[i][j] == x:
                cnt += 1
    nums_lst.append(cnt)
    
print(nums_lst)
    