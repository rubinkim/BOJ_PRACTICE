#-*- coding: utf-8 -*-

"""
7 6
11

7 6
87

100 100
3000


6 6
0
9 64


C, R = map(int, input().split())
K = int(input())

board = [[0] * C for _ in range(R)]
for i in range(0, R):
    for j in range(0, C):
        board[i][j] = (j+1, R-i)
        
lst = []
i = 1
while len(board) > 0:
    board = [list(col) for col in reversed(list(zip(*board)))]

    x = board[-1]
    x.reverse()
    lst.extend(x)
    
    board = board[:-1]
    
#print(lst)

if K <= C * R:    
    print(*(lst[K-1]))
else:
    print(0)
"""
C, R = map(int, input().split())
K = int(input())

if C * R < K:
    print(0)
    
else:
    di = [1, 0, -1, 0]
    dj = [0, 1, 0, -1]

    # 주변을 1로 둘러싸면 범위체크 필요없음
    arr = [[1] * (C+2)] + [[1] + [0] * C + [1] for _ in range(R)] + [[1] * (C+2)]
    ci, cj, dr = 1, 1, 0
    
    for n in range(1, K):           # 관객들에게 배정된 번호표
        arr[ci][cj] = n
        ni, nj = ci + di[dr],  cj + dj[dr]
        # 비어있으면 이동가능
        if arr[ni][nj] == 0:
            ci, cj = ni, nj
        # 범위 밖에 있거나 또는 이미 숫자로 채워져 있으면 방향꺽기
        else:
            dr = (dr + 1) % 4
            ci, cj = ci + di[dr],  cj + dj[dr]       
            
    print(f"{cj} {ci}") 
    