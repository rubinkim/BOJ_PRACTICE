#-*- coding: utf-8 -*-
"""
1 2 4 4
2 3 5 7
3 1 6 5
7 3 8 6

(26)
"""

arr = [[0] * 101 for _ in range(101)]
cnt = 0
for _ in range(4):
    x1, y1, x2, y2 = map(int, input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            if arr[i][j] == 0:
                arr[i][j] = 1
                cnt += 1
print(cnt)