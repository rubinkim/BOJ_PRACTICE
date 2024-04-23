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
    
    for i in range(len(target)):       
        if i == 0 and target[i] == guess[i+1] and not target_chk[i] and not guess_chk[i+1]:
            grey_cnt += 1
            target_chk[i] = True
            guess_chk[i+1] = True
        if 0 < i < len(target)-1 and target[i] == guess[i-1] and not target_chk[i] and not guess_chk[i-1]:
            grey_cnt += 1
            target_chk[i] = True
            guess_chk[i-1] = True
        if 0 < i < len(target)-1 and target[i] == guess[i+1] and not target_chk[i] and not guess_chk[i+1]:
            grey_cnt += 1
            target_chk[i] = True
            guess_chk[i+1] = True
        if i == len(target)-1 and target[i] == guess[i-1] and not target_chk[i] and not guess_chk[i-1]:
            grey_cnt += 1
            target_chk[i] = True
            guess_chk[i-1] = True
            
    for i in range(len(target)):            
        for j in range(len(target)):
            if i <= 1 and target[i] == guess[j] and j >= i+2 and not target_chk[i] and not guess_chk[j]:
                white_cnt += 1
                target_chk[i] = True
                guess_chk[j] = True
            if 1 < i < len(target)-2 and target[i] == guess[j] and (j <= i-2 or j >= i+2) and not target_chk[i] and not guess_chk[j]:
                white_cnt += 1
                target_chk[i] = True
                guess_chk[j] = True
            if i >= len(target)-2 and target[i] == guess[j] and j <= i-2 and not target_chk[i] and not guess_chk[j]:
                white_cnt[i] += 1
                target_chk[i] = True
                guess_chk[j] = True
        
    print(f"{guess}: {black_cnt} black, {grey_cnt} grey, {white_cnt} white")
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
    
    # check black
    for i in range(len(guess)):
        if guess[i] == target[i] and not guess_chk[i] and not target_chk[i]:
            black_cnt += 1
            guess_chk[i] = True
            target_chk[i] = True
            
    # check grey
    for i in range(len(guess)):
        if i == 0 and guess[i] == target[i+1] and not guess_chk[i] and not target_chk[i+1]:
            grey_cnt += 1
            guess_chk[i] = True
            target_chk[i+1] = True
        if 0 < i < len(guess)-1 and guess[i] == target[i-1] and not guess_chk[i] and not target_chk[i-1]:
            grey_cnt += 1
            guess_chk[i] = True
            target_chk[i-1] = True     
        if 0 < i < len(guess)-1 and guess[i] == target[i+1] and not guess_chk[i] and not target_chk[i+1]:
            grey_cnt += 1
            guess_chk[i] = True
            


