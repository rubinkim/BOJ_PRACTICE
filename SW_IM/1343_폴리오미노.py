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
        if cnt % 2 == 1:
            print(-1)
        else:
            if cnt >= 6:
                board[i-cnt : (i-cnt) * (cnt//6)] == 'AAAABB' * (cnt//6)
                cnt -= 6 * (cnt//6)
            
            
