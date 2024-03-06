#-*- coding: utf-8 -*-
"""
3 4
c..c
..c.
....

0 1 2 0
-1 -1 0 1
-1 -1 -1 -1


6 8
.c......
........
.ccc..c.
....c...
..c.cc..
....c...

-1 0 1 2 3 4 5 6
-1 -1 -1 -1 -1 -1 -1 -1
-1 0 0 0 1 2 0 1
-1 -1 -1 -1 0 1 2 3
-1 -1 0 1 0 0 1 2
-1 -1 -1 -1 0 1 2 3


H, W = map(int, input().split())
joi = [[0] * W for _ in range(H)]
for i in range(H):
    row = input()
    for j in range(W):
        joi[i][j] = row[j]    
    
for row in joi:
    print(row)

#print(joi)
print(len(joi))
print(len(joi[0]))
print(joi[0][1])
"""

#lst = ['.', 'c', 'c', 'c', '.', '.', 'c', '.']
lst = ['.', '.', 'c', 'c', '.', 'c', '.', '.', '.', 'c']
cloudy = [-5] * len(lst)

#print(lst)
#print(cloudy)

for i in range(len(lst)):
    if lst[i] == '.':
        cloudy[i] = -1
    if lst[i] == 'c':
        cloudy[i] = 0
        cnt = 1
        for j in range(i+1, len(lst)):
            cloudy[j] = cnt
            cnt += 1
            if lst[j] == 'c':
                new_c = j
                cnt = 1
                break
            