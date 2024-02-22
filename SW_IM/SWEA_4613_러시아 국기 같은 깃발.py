#-*- coding: utf-8 -*-

"""
2
4 5
WRWRW
BWRWB
WRWRW
RWBWR
6 14
WWWWWWWWWWWWWW
WWRRWWBBBBBBWW
WRRRWWWBWWWWRB
WWBWBWWWBWRRRR
WBWBBWWWBBWRRW
WWWWWWWWWWWWWW
"""
def count_color(w, b, arr, n, m):
    cnt = 0
    cnt += sum([sum([arr[i][j] != 'W' for j in range(m)]) for i in range(w+1)])
    cnt += sum([sum([arr[i][j] != 'B' for j in range(m)]) for i in range(w+1, b+1)])
    cnt += sum([sum([arr[i][j] != 'R' for j in range(m)]) for i in range(b+1, n)])
    return cnt

TC = int(input())
for no in range(TC):
    N, M = map(int, input().split())
    arr = [[""] * M for _ in range(N)]
    for i in range(N):
        for j, x in enumerate(input()):
            arr[i][j] = x        

    cnt_lst = []
    for x in range(N-2):
        for y in range(x+1, N-1):
            cnt_lst.append(count_color(x, y, arr, N, M))
    print(f"#{no+1} {min(cnt_lst)}")        

