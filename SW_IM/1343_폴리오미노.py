#-*- coding: utf-8 -*-
"""
XX.XXXXXXXXXX..XXXXXXXX...XXXXXX

(BB.AAAAAAAABB..AAAAAAAA...AAAABB)
"""
board = input()
cnt = 0
poly = []

for i, ch in enumerate(board):
    if ch == 'X':
        cnt += 1
    elif ch == '.':
        if cnt % 6 == 0:
            poly.append('AAAABB' *  (cnt//6))
            poly.append(ch)
            cnt = 0
        elif cnt % 4 == 0:
            poly.append('AAAA' * (cnt//4))
            poly.append(ch)
            cnt = 0
        elif cnt % 2 == 0:
            poly.append('BB' * (cnt//2))
            poly.append(ch)
            cnt = 0
        else:
            print(-1)
print(*poly)
            
