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
    guess_chk = [False] * len(guess)
    
    for i in range(len(target)):
        if target[i] == guess[i] and not target_chk[i] and not guess_chk[i]:
            black_cnt += 1
            target_chk[i] = True
            guess_chk[i] = True
            
        if i == 0 and target[i] == guess[i+1] and not target_chk[i] and not guess_chk[i+1]:
            grey_cnt += 1
            target_chk[i] = True
            guess_chk[i+1] = True
        elif 0 < i < len(target)-1 and target[i] == guess[i-1] and not target_chk[i] and not guess_chk[i-1]:
            grey_cnt += 1
            target_chk[i] = True
            guess_chk[i-1] = True
        elif 0 < i < len(target)-1 and target[i] == guess[i+1] and not target_chk[i] and guess_chk[i+1]:
            grey_cnt += 1
            target_chk[i] = True
            guess_chk[i+1] = True
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
        



