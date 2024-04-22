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
    
    black_cnt, grey_cnt = 0, 0
    for i in range(len(target)):
        if target[i] == guess[i]:
            black_cnt += 1
        if i == 0 and target[i] == guess[i+1]:
            grey_cnt += 1
        elif 0 < i < len(target)-1 and (target[i] == guess[i-1] or target[i] == guess[i+1]):
            grey_cnt += 1
        elif i == len(target)-1:
            
        
    print(f"{guess}: {black_cnt} black")
        



