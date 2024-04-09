#-*- coding: utf-8 -*-
"""
XX.XXXXXXXXXX..XXXXXXXX...XXXXXX

(BB.AAAAAAAABB..AAAAAAAA...AAAABB)
"""
board = list(input())
cnt = 0
poly = []

for i, ch in enumerate(board):
    if ch == 'X':
        cnt += 1
    elif ch == '.':
        poly.append(cnt)
        cnt = 0
print(poly)
            
            
