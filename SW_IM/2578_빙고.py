#-*- coding: utf-8 -*-

"""
11 12 2 24 10
16 1 13 3 25
6 20 5 21 17
19 4 8 14 9
22 15 7 23 18
5 10 7 16 2
4 22 8 17 13
3 18 1 6 25
12 19 23 14 21
11 24 9 20 15
"""

bingo = []
calls = []


for i in range(10):    
    if i < 5:
        bingo.append(list(map(int, input().split())))
    else:
        calls.extend(list(map(int, input().split())))        

d0 = [bingo[i][i] for i in range(5)]
d1 = [bingo[4-i][i] for i in range(5)]

cnt = 0

for x in calls:
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == x:
                bingo[i][j] = 0
                if sum(bingo[i]) == 0:
                    cnt += 1                    
                if sum([bingo[x][j] for x in range(5)]) == 0:
                    cnt += 1
                if sum([bingo[k][k] for k in range(5)]) == 0:
                    cnt += 1
                if sum([bingo[4-k][k] for k in range(5)]) == 0:
                    cnt += 1
                if cnt == 3:
                    print(f"x : {x},  cnt : {cnt}, x의 인덱스 : {calls.index(x) + 1}")
                    for rr in bingo:
                        print(rr)
                break
        

    


                
    