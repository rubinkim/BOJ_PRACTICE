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
"""

C, R = map(int, input().split())
K = int(input())

board = [[0] * C for _ in range(R)]
for i in range(0, R):
    for j in range(0, C):
        board[i][j] = (j+1, R-i)
        
for row in board:
    print(row)

print()   
print(board[0][:])
print(len(board[0][:]))

#board = board - board[0][:]
#board = board - board[:][0]
#board = board - board[-1][:]
#board = board - board[:][-1]
print()
print(board[:][0])
print(len(board[:][0]))
print()
print(board[0][:] + board[:][0])
