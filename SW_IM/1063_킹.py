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