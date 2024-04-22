#-*- coding: utf-8 -*-
"""
ABCD AAAA
ABCD ACEB
ABCD EFBB
ABCD ACBC
ABCD BEAA
ABCD ABCD
ABABAA BCBCAA
#

AAAA: 1 black, 0 grey, 0 white
ACEB: 1 black, 1 grey, 1 white
EFBB: 0 black, 1 grey, 0 white
ACBC: 1 black, 2 grey, 0 white
BEAA: 0 black, 1 grey, 1 white
ABCD: 4 black, 0 grey, 0 white
BCBCAA: 2 black, 2 grey, 0 white
"""

import os
client_sock=socket(AF_INET, SOCK_STREAM)
try:
    client_sock.connect((Host,Port))

except ConnectionRefusedError:
    print('서버에 연결할 수 없습니다.')
    print('1. 서버의 ip주소와 포트번호가 올바른지 확인하십시오.')
    print('2. 서버 실행 여부를 확인하십시오.')
    os._exit(1)

while True:
    arrangement = input()
    if arrangement == "#":
        break

    target, guess = arrangement.split()
    print(f"target : {target},  guess : {guess}")
    
    black_cnt, grey_cnt, white_cnt = 0, 0, 0
    chk = [False] * len(target)
    
    for i in range(len(target)):
        if target[i] == guess[i] and not chk[i]:
            black_cnt += 1
            chk[i] = True
            
        if i == 0 and target[i] == guess[i+1] and not chk[i]:
            grey_cnt += 1
            chk[i] = True
        elif 0 < i < len(target)-1 and (target[i] == guess[i-1] or target[i] == guess[i+1]) and not chk[i]:
            grey_cnt += 1
            chk[i] = True
        elif i == len(target)-1 and target[i] == guess[i-1] and not chk[i]:
            grey_cnt += 1
            chk[i] = True
            
        if i <= 1 and any([target[i] == guess[j] for j in range(i+2, len(target))]) and not chk[i]:
            white_cnt += 1
            chk[i] = True
        elif 1 < i < len(target)-2 and (any([target[i] == guess[j] for j in range(i+2, len(target))]) or any([target[i] == guess[j] for j in range(i-1)])) and not chk[i]:
            white_cnt += 1
            chk[i] = True
        elif i >= len(target)-2 and any([target[i] == guess[j] for j in range(i-1)]) and not chk[i]:
            white_cnt += 1
            chk[i] = True
        
    print(f"{guess}: {black_cnt} black, {grey_cnt} grey, {white_cnt} white")
        



