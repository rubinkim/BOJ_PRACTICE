#-*- coding: utf-8 -*-
"""
A1 A2 5
B
L
LB
RB
LT

(A1, A2)


A1 H8 1
T

(A2, H8)



A1 A2 1
T

(A2, A3)


A1 A2 2
T
R

(B2, A3)



A8 B7 18
RB
RB
RB
RB
RB
RB
RB
RB
RB
RB
RB
RB
RB
RB
RB
RB
RB
RB

(G2, H1)



C1 B1 3
L
T
LB

(B2, A1)

"""

king, stone, N = input().split()
N = int(N)
print(f"king : {king},  stone : {stone},  N : {N}")

board = [[0] * 8 for _ in range(8)]
row = '87654321'
col = 'ABCDEFGH'
for i in range(len(row)):
    for j in range(len(col)):
        board[i][j] = col[j] + row[i]

for row in board:
    print(row)
    
directions = ['R', 'L', 'B', 'T', 'RT', 'LT', 'RB', 'LB']
moves = [(0, 1), (0, -1), (1, 0), (-1, 0), (-1, 1), (-1, -1), (1, 1), (1, -1)]

moves_dict = {}
for k, v in zip(directions, moves):
    moves_dict[k] = v
    
print(moves_dict)

def convert_to_idx(x):
    return (8 - int(x[1]), ord(x[0]) - 65)

def convert_to_position(y, x):
    new_y = str(8 - y)
    new_x = chr(x + 65)
    return new_x + new_y 

king_y, king_x = convert_to_idx(king)
stone_y, stone_x = convert_to_idx(stone)

for _ in range(N):
    dy, dx = moves_dict[input()]
    if king_y + dy < 0 or king_y + dy >= 8 or king_x + dx < 0 or king_x + dx >= 8:
        continue
    if 0 <= king_y + dy < 8 and 0 <= king_x + dx < 8:
        if king_y + dy != stone_y and king_x + dx != stone_x:
            king_y += dy
            king_x += dx
        if king_y + dy == stone_y and king_x + dx == stone_x and 0 <= stone_y + dy < 8 and 0 <= stone_x + dx < 8:
            king_y += dy
            king_x += dx
            stone_y += dy
            stone_y += dx
        if king_y + dy == stone_y and king_x + dx == stone_x and (stone_y + dy < 0 or stone_y + dy >= 8 or stone_x + dx < 0 or stone_x + dx >= 8):
            continue
        

print(convert_to_position(*(king_y, king_x)))
print(convert_to_position(*(stone_y, stone_x)))