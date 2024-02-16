#-*- coding: utf-8 -*-
"""
4
0 1 2 3
4 0 5 6
7 1 0 2
3 4 5 0

6
0 1 2 3 4 5
1 0 2 3 4 5
1 2 0 3 4 5
1 2 3 0 4 5
1 2 3 4 0 5
1 2 3 4 5 0

8
0 5 4 5 4 5 4 5
4 0 5 1 2 3 4 5
9 8 0 1 2 3 1 2
9 9 9 0 9 9 9 9
1 1 1 1 0 1 1 1
8 7 6 5 4 0 3 2
9 1 9 1 9 1 0 9
6 5 4 3 2 1 9 0
"""

N = int(input())
arr = [list(map(int, input().split())) for _  in range(N)]
M = N // 2
ans = 100 * M * M

def dfs(n, alst, blst):      # n : 사람번호,  alst(blst) : a(b)팀을 선택한 사람들을 저장할 리스트
    global ans
    if n == N:
        ans = min(ans, cal(alst, blst))
        return
    
    dfs(n+1, alst+[n], blst)
    dfs(n+1, alst, blst+[n])

def cal(alst, blst):
    asm = bsm = 0
    for i in range(M):
        for j in range(M):
            asm += arr[alst[i]][alst[j]]
            bsm += arr[blst[i]][blst[j]]
    return abs(asm - bsm)

dfs(0, [], [])
print(ans)

    
    
        
        