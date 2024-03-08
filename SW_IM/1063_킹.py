#-*- coding: utf-8 -*-
"""
A1 A2 5
B
L
LB
RB
LT

(A1, A2)
"""

king, stone, N = input().split()
king_x, king_y = ord(king[0]) - 64, int(king[1])
stone_x, stone_y = ord(stone[0]) - 64, int(stone[1])
print(f"king : {king},  stone : {stone},  N : {N}")
print(f"king_x : {king_x},  king_y : {king_y},  stone_x : {stone_x},  stone_y : {stone_y}")

board = [[0] * 8 for _ in range(8)]
row = '87654321'
col = 'ABCDEFGH'
for j in range(len(col)):
    for i in range(len(row)):
        board[i][j] = col[i] + row[j]

for row in board:
    print(row)
    
directions = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
moves = [()]