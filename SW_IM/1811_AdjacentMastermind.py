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

while True:
    arrangement = input()
    if arrangement == "#":
        break

    target, guess = arrangement.split()
    print(f"target : {target},  guess : {guess}")
    
    black_cnt, grey_cnt, white_cnt = 0, 0, 0
    target_chk = [False] * len(target)

    
    for i in range(len(target)):
        if target[i] == guess[i] and not target_chk[i]:
            black_cnt += 1
            target_chk[i] = True

    for i in range(len(target)):       
        if i == 0 and target[i] == guess[i+1] and not target_chk[i]:
            grey_cnt += 1
            target_chk[i] = True

        elif 0 < i < len(target)-1 and target[i] == guess[i-1] and not target_chk[i]:
            grey_cnt += 1
            target_chk[i] = True

        elif 0 < i < len(target)-1 and target[i] == guess[i+1] and not target_chk[i]:
            grey_cnt += 1
            target_chk[i] = True

        elif i == len(target)-1 and target[i] == guess[i-1] and not target_chk[i]:
            grey_cnt += 1
            target_chk[i] = True
           
    for i in range(len(target)):
        for j in range(len(target)):
            if i <= 1 and target[i] == guess[j] and j >= i+2 and not target_chk[i]:
                white_cnt += 1
                target_chk[i] = True

            if 1 < i < len(target)-2 and target[i] == guess[j] and (j <= i-2 or j >= i+2) and not target_chk[i]:
                white_cnt += 1
                target_chk[i] = True

            if i >= len(target)-2 and target[i] == guess[j] and j <= i-2 and not target_chk[i]:
                white_cnt[i] += 1
                target_chk[i] = True

        
    print(f"{guess}: {black_cnt} black, {grey_cnt} grey, {white_cnt} white")
        



