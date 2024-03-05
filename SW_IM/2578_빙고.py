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
print()
for row in bingo:
    print(row)
print()
print(calls)
print()       

cnt = 0

for x in calls:
    flag = False
    for i in range(5):
        for j in range(5):
            if bingo[i][j] == x:
                bingo[i][j] = 0
                if sum(bingo[i]) == 0:
                    cnt += 1                    
                if sum([bingo[x][j] for x in range(5)]) == 0:
                    cnt += 1
                if (i,j) in [(0,0), (1,1), (2,2), (3,3), (4,4)] and sum([bingo[k][k] for k in range(5)]) == 0:
                    cnt += 1
                if (i,j) in [(4,0), (3,1), (2,2), (1,3), (0,4)] and sum([bingo[4-k][k] for k in range(5)]) == 0:
                    cnt += 1
                if cnt >= 3:
                    print(calls.index(x)+1)
                    exit(0)        

                flag = True
                break
        if flag1 == True:
            break



"""
x = [11,42,30,14]
y = [-1,-2,-3,-4]
z = [1,2,3,4,5]

cnt = 0
flag = False
for x_val in x:
    for i in range(4):
        for j in range(4):
            if (i, j) in [(2,0), (0,1), (1,1)]:
                cnt += 1     
                print(f"x_val : {x_val}, cnt : {cnt}, {(i,j)}")
                flag = True
                break
        if flag == True:
            break                    
             
print()
print(cnt)
"""                    
        

    


                
    