#-*- coding: utf-8 -*-

"""
7 6
11

7 6
87

100 100
3000


6 6
0
9 64


C, R = map(int, input().split())
K = int(input())

board = [[0] * C for _ in range(R)]
for i in range(0, R):
    for j in range(0, C):
        board[i][j] = (j+1, R-i)
        
lst = []
i = 1
while len(board) > 0:
    board = [list(col) for col in reversed(list(zip(*board)))]

    x = board[-1]
    x.reverse()
    lst.extend(x)
    
    board = board[:-1]
    
#print(lst)

if K <= C * R:    
    print(*(lst[K-1]))
else:
    print(0)
"""
C, R = map(int, input().split())
K = int(input())

if C * R < K:
    print(0)
    
else:
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]
