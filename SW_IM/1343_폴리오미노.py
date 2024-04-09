#-*- coding: utf-8 -*-
"""
XX.XXXXXXXXXX..XXXXXXXX...XXXXXX

(BB.AAAAAAAABB..AAAAAAAA...AAAABB)
"""
board = list(input())
cnt = 0
poly = []

for i, ch in enumerate(board):
    print(i, end=' ')
    if ch == 'X':
        cnt += 1
    elif ch == '.':
        poly.append(cnt)
        cnt = 0
    if i == len(board)-1 and board[-1] == 'X':
        print(True)
        poly.append(cnt)
print(poly)
print(cnt)
print(len(board))
print(board[-1])

            
            
